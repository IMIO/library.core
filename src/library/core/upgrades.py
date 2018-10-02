# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone.app.upgrade.utils import loadMigrationProfile
from zope.annotation.interfaces import IAnnotations
import logging


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-library.core:default',
    )


def purge_patrimoine_scales(context):
    logger = logging.getLogger('library.core')
    pc = getToolByName(context, 'portal_catalog')
    for brain in pc(portal_type='patrimoine'):
        patrimoine = brain.getObject()
        annotations = IAnnotations(patrimoine)
        if 'plone.scale' in annotations:
            del annotations['plone.scale']
            logger.info('purged {0}'.format(patrimoine.id))
    logger.info('scales purge over.')
