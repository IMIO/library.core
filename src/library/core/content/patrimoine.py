# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.dexterity.browser import view
from plone.supermodel import model
from zope.interface import implementer
from plone.autoform import directives as form

from library.core.widget.textdate import TextDateFieldWidget


class IPatrimoine(model.Schema):
    """ Marker interface for Patrimoine
    """

    model.load('patrimoine.xml')
    form.widget('date', TextDateFieldWidget)


@implementer(IPatrimoine)
class Patrimoine(Container):
    """
    """


class PatrimoineView(view.DefaultView):
    """
    """
