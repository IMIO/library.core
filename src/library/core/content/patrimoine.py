# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IPatrimoine(model.Schema):
    """ Marker interface for Patrimoine
    """

    model.load('patrimoine.xml')


@implementer(IPatrimoine)
class Patrimoine(Container):
    """
    """
