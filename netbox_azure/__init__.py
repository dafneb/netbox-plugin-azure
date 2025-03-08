#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from netbox.plugins import PluginConfig

class NetBoxAzureConfig(PluginConfig):
    name = 'netbox_azure'
    verbose_name = 'NetBox Azure Inventory'
    version = '1.0.0'
    author = 'David Burel'
    description = 'Azure integration for NetBox'
    base_url = 'azure-inventory'
    required_settings = []
    default_settings = {}

config = NetBoxAzureConfig
