#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the models for the netbox_azure app
"""

from django.db import models
from netbox.models import NetBoxModel
from .choices import SubscriptionStatusChoices

class AzureTenantModel(NetBoxModel):
    """Azure Tenant Model
    """
    tenid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)

    class Meta:
        """Meta data for the AzureTenantModel
        """
        ordering = ('name',)

    def __str__(self):
        return f'{self.tenid} {self.name}'

class AzureSubscriptionModel(NetBoxModel):
    """Azure Subscription Model
    """
    subid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    status = models.CharField(
        max_length=25,
        choices=SubscriptionStatusChoices,
        default=SubscriptionStatusChoices.STATUS_ACTIVE
    )
    approver = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    tenant = models.ForeignKey(AzureTenantModel, on_delete=models.CASCADE)

    class Meta:
        """Meta data for the AzureSubscriptionModel
        """
        ordering = ('name',)

    def __str__(self):
        return f'{self.subid} {self.name} [{self.status}]'

    def get_status_color(self):
        return SubscriptionStatusChoices.colors.get(self.status)
