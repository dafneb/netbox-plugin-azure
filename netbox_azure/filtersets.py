#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the filter sets for the netbox_azure app
"""

from netbox.filtersets import NetBoxModelFilterSet
from netbox_azure import models

class AzureSubscriptionFilterSet(NetBoxModelFilterSet):
    """Filter set for the AzureSubscriptionModel
    """

    class Meta:
        """Meta data for the AzureSubscriptionFilterSet
        """
        model = models.AzureSubscriptionModel
        fields = ['subid', 'name', 'status', 'approver', 'owner', 'tenant']

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
