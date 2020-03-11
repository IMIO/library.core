# -*- coding: utf-8 -*-
from collective.taxonomy.interfaces import ITaxonomy
from datetime import datetime
from library.core.widget.textdate import TextDateFieldWidget
from plone.app.textfield.value import IRichTextValue
from plone.autoform import directives as form
from plone.dexterity.browser import view
from plone.dexterity.content import Container
from plone.dexterity.utils import iterSchemata
from plone.indexer.decorator import indexer
from plone.supermodel import model
from Products.CMFPlone.utils import getToolByName
from re import match
from z3c.form.validator import SimpleFieldValidator
from zope.component import queryUtility
from zope.interface import implementer
from zope.interface import Invalid
from zope.schema import getFields

import six


class IPatrimoine(model.Schema):
    """ Marker interface for Patrimoine
    """

    model.load("patrimoine.xml")
    form.widget("date", TextDateFieldWidget)


class DateValidator(SimpleFieldValidator):

    regex_formats = {
        "\d{8}$": "%d%m%Y",
        "\d{6}$": "%m%Y",
        "\d{4}$": "%Y",
        "\d{1,2}/\d{1,2}/\d{4}$": "%d/%m/%Y",
        "\d{1,2}/\d{4}$": "%m/%Y",
        "\d{1,2}-\d{1,2}-\d{4}$": "%d-%m-%Y",
        "\d{1,2}-\d{4}$": "%m-%Y",
    }

    def validate(self, value, force=False):
        super(DateValidator, self).validate(value, force)
        if value:
            stripped = value.strip()
            for regex, datetime_format in self.regex_formats.items():
                if match(regex, stripped):
                    try:
                        test = datetime.strptime(stripped, datetime_format).date()
                        return True
                    except ValueError as e:
                        raise Invalid(u"Date invalide")
            raise Invalid(
                u"Format d'encodage non reconnu (jour/mois/année, mois/année ou année)"
            )


@implementer(IPatrimoine)
class Patrimoine(Container):
    """
    """


class PatrimoineView(view.DefaultView):
    """
    """


@indexer(IPatrimoine)
def searchabletext_patrimoine(object, **kw):
    """
    Indexes the following field types in Patrimoine objects,
    making them available in Full Text Search:
    - text
    - rich text
    - keywords
    - taxonomies
    """
    result = []
    subjects = getattr(object, "subject", None)
    if type(subjects) is tuple:
        text = " ".join([s for s in subjects if isinstance(s, six.text_type)])
        result.append(text.encode("utf-8"))

    for schemata in iterSchemata(object):
        if "collective.taxonomy.generated" in str(schemata):
            value = getattr(object, "taxonomy_{}".format(schemata.__name__), None)
            if value:
                value = [value] if isinstance(value, six.text_types) else value
                translator = queryUtility(
                    ITaxonomy, name="collective.taxonomy.{}".format(schemata.__name__)
                )
                for taxonomy_id in value:
                    translation = translator.translate(
                        taxonomy_id, target_language="fr"
                    )
                    text = translation
                    result.append(text)
            continue

        for field_name, field_type in getFields(schemata).items():
            value = getattr(object, field_name, None)
            if isinstance(value, six.text_type):
                text = value
                result.append(text)
            elif IRichTextValue.providedBy(value):
                transforms = getToolByName(object, "portal_transforms")
                text = (
                    transforms.convertTo(
                        "text/plain", value.raw, mimetype=value.mimeType
                    )
                    .getData()
                    .strip()
                )
                result.append(text)

    return " ".join(result)
