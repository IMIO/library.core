# -*- coding: utf-8 -*-
"""Setup tests for this package."""

from bibliotheca.core.testing import BIBLIOTHECA_CORE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that bibliotheca.core is properly installed."""

    layer = BIBLIOTHECA_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if bibliotheca.core is installed."""
        self.assertTrue(self.installer.is_product_installed("bibliotheca.core"))

    def test_browserlayer(self):
        """Test that IBibliothecaCoreLayer is registered."""
        from bibliotheca.core.interfaces import IBibliothecaCoreLayer
        from plone.browserlayer import utils

        self.assertIn(IBibliothecaCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = BIBLIOTHECA_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("bibliotheca.core")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if bibliotheca.core is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("bibliotheca.policy"))

    def test_browserlayer_removed(self):
        """Test that IBibliothecaCoreLayer is removed."""
        from bibliotheca.core.interfaces import IBibliothecaCoreLayer
        from plone.browserlayer import utils

        self.assertNotIn(IBibliothecaCoreLayer, utils.registered_layers())
