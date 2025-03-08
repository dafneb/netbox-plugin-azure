#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='netbox-azure',
    version='1.0.0',
    description='Azure integration for NetBox',
    url='https://github.com/dafneb/netbox-plugin-azure',
    author='David Burel',
    author_email='david.burel@burelovi.eu',
    license="MIT License",
    install_requires=[
        #'azure-core==1.32.0',
        #'azure-identity==1.20.0',
        #'azure-mgmt-core==1.5.0',
        #'azure-mgmt-alertsmanagement==1.0.0',
        #'azure-mgmt-monitor==6.0.2',
        #'azure-mgmt-authorization==4.0.0',
        #'azure-mgmt-billing==7.0.0',
        #'azure-mgmt-costmanagement==4.0.1',
        #'azure-mgmt-subscription==3.1.1',
        #'azure-mgmt-resource==23.3.0',
        #'azure-mgmt-compute==34.0.0',
        #'azure-mgmt-network==28.1.0',
        #'azure-mgmt-storage==22.1.1',
        #'azure-mgmt-appconfiguration==4.0.0',
        #'azure-mgmt-web==8.0.0',
        #'azure-mgmt-containerservice==34.1.0'
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
