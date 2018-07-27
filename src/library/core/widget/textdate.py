# encoding: utf8

from datetime import datetime
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget, NO_VALUE, IDataConverter
from z3c.form.widget import FieldWidget
from zope.interface import implementer
from plone.app.z3cform.interfaces import IDateWidget

from zope.component import adapts
from zope.schema.interfaces import IDate
from z3c.form.converter import BaseDataConverter


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

    def toWidgetValue(self, value):
        if value is self.field.missing_value:
            return u''
        return value.strftime('%d/%m/%Y')

    def toFieldValue(self, value):
        if value == u'':
            return self.field.missing_value

        stripped = value.strip()
        if len(stripped) == 8:
            return datetime.strptime(stripped, '%d%m%Y').date()
        else:
            return datetime.strptime(stripped, '%d/%m/%Y').date()
