# -*- coding: utf-8 -*-
from datetime import datetime
from plone.app.textfield.value import IRichTextValue
from plone.autoform import directives as form
from plone.dexterity.content import Container
from plone.dexterity.browser import view
from plone.dexterity.utils import iterSchemata
from plone.indexer.decorator import indexer
from plone.supermodel import model
from re import match
from zope.interface import implementer
from zope.interface import Invalid
from zope.schema import getFields
from z3c.form.validator import SimpleFieldValidator
from Products.CMFPlone.utils import safe_unicode
from Products.CMFPlone.utils import getToolByName

from library.core.widget.textdate import TextDateFieldWidget


class IPatrimoine(model.Schema):
    """ Marker interface for Patrimoine
    """

    model.load('patrimoine.xml')
    form.widget('date', TextDateFieldWidget)


class DateValidator(SimpleFieldValidator):

    regex_formats = {
        '\d{8}$': '%d%m%Y',
        '\d{6}$': '%m%Y',
        '\d{4}$': '%Y',
        '\d{1,2}/\d{1,2}/\d{4}$': '%d/%m/%Y',
        '\d{1,2}/\d{4}$': '%m/%Y',
        '\d{1,2}-\d{1,2}-\d{4}$': '%d-%m-%Y',
        '\d{1,2}-\d{4}$': '%m-%Y',
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
                        raise Invalid(u'Date invalide')
            raise Invalid(u'Format d\'encodage non reconnu (jour/mois/année, mois/année ou année)')


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
    Indexes every text and rich text field (+ keywords) in Patrimoine objects,
    making them available in Full Text Search.
    """
    result = []
    subjects = getattr(object, 'subject', None)
    if type(subjects) is tuple:
        text = ' '.join([safe_unicode(s)
                         for s in subjects
                         if type(safe_unicode(s) is unicode)])
        result.append(text.encode('utf-8'))

    for schemata in iterSchemata(object):
        for field_name, field_type in getFields(schemata).items():
            value = getattr(object, field_name, None)
            if type(value) is unicode:
                text = safe_unicode(value).encode('utf-8')
                result.append(text)
            elif IRichTextValue.providedBy(value):
                transforms = getToolByName(object, 'portal_transforms')
                text = transforms.convertTo(
                    'text/plain',
                    safe_unicode(value.raw).encode('utf-8'),
                    mimetype=value.mimeType,
                ).getData().strip()
                result.append(text)

    return ' '.join(result)
