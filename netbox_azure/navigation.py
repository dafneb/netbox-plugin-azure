#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the navigation menu for the netbox_azure app"""

from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label="Azure",
    groups=(
        (
            "Azure Inventory",
            (
                PluginMenuItem(
                    link="plugins:netbox_azure:azuretenantmodel_list",
                    link_text="Tenants",
                    buttons=(
                        PluginMenuButton(
                            "plugins:netbox_azure:azuretenantmodel_add",
                            "Add",
                            "mdi mdi-plus-thick",
                        ),
                        # PluginMenuButton('plugins:netbox_branching:branch_bulk_import', 'Import', 'mdi mdi-upload'),
                    ),
                ),
                PluginMenuItem(
                    link="plugins:netbox_azure:azuresubscriptionmodel_list",
                    link_text="Subscriptions",
                    buttons=(
                        PluginMenuButton(
                            "plugins:netbox_azure:azuresubscriptionmodel_add",
                            "Add",
                            "mdi mdi-plus-thick",
                        ),
                        # PluginMenuButton('plugins:netbox_branching:branch_bulk_import', 'Import', 'mdi mdi-upload'),
                    ),
                ),
            ),
        ),
    ),
    icon_class="mdi mdi-microsoft-azure",
)
