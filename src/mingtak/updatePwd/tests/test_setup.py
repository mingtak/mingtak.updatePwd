# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from mingtak.updatePwd.testing import MINGTAK_UPDATEPWD_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingtak.updatePwd is properly installed."""

    layer = MINGTAK_UPDATEPWD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingtak.updatePwd is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingtak.updatePwd'))

    def test_browserlayer(self):
        """Test that IMingtakUpdatepwdLayer is registered."""
        from mingtak.updatePwd.interfaces import (
            IMingtakUpdatepwdLayer)
        from plone.browserlayer import utils
        self.assertIn(IMingtakUpdatepwdLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGTAK_UPDATEPWD_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['mingtak.updatePwd'])

    def test_product_uninstalled(self):
        """Test if mingtak.updatePwd is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingtak.updatePwd'))

    def test_browserlayer_removed(self):
        """Test that IMingtakUpdatepwdLayer is removed."""
        from mingtak.updatePwd.interfaces import \
            IMingtakUpdatepwdLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMingtakUpdatepwdLayer, utils.registered_layers())
