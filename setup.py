# -*- coding: utf-8 -*-
"""Installer for the library.core package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="library.core",
    version="2.1.7.dev0",
    description="Core package for Bibliotheca",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Nicolas Demonte",
    author_email="support@imio.be",
    url="https://pypi.python.org/pypi/library.core",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["library"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        "plone.api>=1.8.4",
        "plone.restapi",
        "Products.GenericSetup>=1.8.2",
        "setuptools",
        "z3c.jbot",
        "z3c.unconfigure",
        "plone.app.discussion",
        "collective.behavior.gallery",
        "collective.geolocationbehavior",
        "collective.taxonomy",
        "collective.z3cform.select2>=3.0.0b6",
        "collective.faceted.map",
        "iaweb.mosaic",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.restapi",
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = library.core.locales.update:update_locale
    """,
)
