# encoding: utf8

from datetime import datetime
from re import match
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget, NO_VALUE, IDataConverter
from z3c.form.widget import FieldWidget
from zope.interface import implementer
from plone.app.z3cform.interfaces import IDateWidget

from zope.component import adapts
from zope.schema.interfaces import IDate
from z3c.form.converter import BaseDataConverter
from z3c.form.converter import FormatterValidationError


class ITextDateWidget(IDateWidget):
    """Marker interface for TextDate"""


@implementer(ITextDateWidget)
class TextDateWidget(TextWidget):
    pass


@implementer(IFieldWidget)
def TextDateFieldWidget(field, request):
    """IFieldWidget factory for TextDateWidget."""
    return FieldWidget(field, TextDateWidget(request))


@implementer(IDataConverter)
class TextDateConverter(BaseDataConverter):
    """Text field <-> python datetime (rounded to te day)"""

    adapts(
        IDate,
        ITextDateWidget,
    )

    regex_formats = {
        '\d{8}$': '%d%m%Y',
        '\d{6}$': '%m%Y',
        '\d{4}$': '%Y',
        '\d{1,2}/\d{1,2}/\d{4}$': '%d/%m/%Y',
        '\d{1,2}/\d{4}$': '%m/%Y',
    }

    def toWidgetValue(self, value):
        if value is self.field.missing_value:
            return u''
        return '{v.day:02d}/{v.month:02d}/{v.year}'.format(v=value)

    def toFieldValue(self, value):
        if value == u'':
            return self.field.missing_value

        stripped = value.strip()
        for regex, datetime_format in self.regex_formats.items():
            if match(regex, stripped):
                try:
                    return datetime.strptime(stripped, datetime_format).date()
                except ValueError as e:
                    raise FormatterValidationError(u'Date invalide', value)
        raise FormatterValidationError(u'Format d\'encodage non reconnu (jour/mois/année, mois/année ou année)', value)
