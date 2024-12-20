# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import library.core


class LibraryCoreLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.

        self.loadZCML(name="testing.zcml", package=library.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "library.core:default")


LIBRARY_CORE_FIXTURE = LibraryCoreLayer()


LIBRARY_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LIBRARY_CORE_FIXTURE,), name="LibraryCoreLayer:IntegrationTesting"
)


LIBRARY_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LIBRARY_CORE_FIXTURE,), name="LibraryCoreLayer:FunctionalTesting"
)


LIBRARY_CORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(LIBRARY_CORE_FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="LibraryCoreLayer:AcceptanceTesting",
)
