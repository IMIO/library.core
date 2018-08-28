# -*- coding: utf-8 -*-
from datetime import datetime
from plone.dexterity.content import Container
from plone.dexterity.browser import view
from plone.supermodel import model
from re import match
from zope.interface import implementer
from zope.interface import Invalid
from z3c.form.validator import SimpleFieldValidator


class IPatrimoine(model.Schema):
    """ Marker interface for Patrimoine
    """

    model.load('patrimoine.xml')


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
