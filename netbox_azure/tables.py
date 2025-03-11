#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the tables for the netbox_azure app
"""

import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import AzureTenantModel, AzureSubscriptionModel

class AzureTenantTable(NetBoxTable):
    """Table for Azure Tenant Model
    """
    tenid = tables.Column(
        linkify=True,
        verbose_name='Tenant ID'
    )
    name = tables.Column(
        linkify=True,
        verbose_name='Tenant Name'
    )
    comment = tables.Column(
        verbose_name='Comment'
    )

    class Meta(NetBoxTable.Meta):
        """Meta data for the AzureTenantTable
        """
        model = AzureTenantModel
        fields = ('pk', 'id', 'tenid', 'name', 'comment')
        default_columns = ('tenid', 'name', 'comment')

class AzureSubscriptionTable(NetBoxTable):
    """Table for Azure Subscription Model
    """
    subid = tables.Column(
        linkify=True,
        verbose_name='Subscription ID'
    )
    name = tables.Column(
        linkify=True,
        verbose_name='Subscription Name'
    )
    comment = tables.Column(
        verbose_name='Comment'
    )
    status = ChoiceFieldColumn(
        verbose_name='Status'
    )
    approver = tables.Column(
        verbose_name='Approver'
    )
    owner = tables.Column(
        verbose_name='Owner'
    )
    tenant = tables.Column(
        linkify=True,
        verbose_name='Tenant'
    )

    class Meta(NetBoxTable.Meta):
        """Meta data for the AzureSubscriptionTable
        """
        model = AzureSubscriptionModel
        fields = ('pk', 'id', 'subid', 'name', 'comment', 'status', 'approver', 'owner', 'tenant')
        default_columns = ('subid', 'name', 'comment', 'status', 'approver', 'owner')
