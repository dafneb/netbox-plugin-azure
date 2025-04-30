#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the models for the netbox_azure app
"""

from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_azure import choices

class AzureTenantModel(NetBoxModel):
    """Azure Tenant Model
    """
    tenid = models.CharField(
        max_length=50
    )
    name = models.CharField(
        max_length=50
    )
    comment = models.TextField(
        blank=True
    )

    class Meta:
        """Meta data for the AzureTenantModel
        """
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.tenid})'

    def get_absolute_url(self):
        """Return the URL to access a particular instance of the model
        """
        return reverse('plugins:netbox_azure:azuretenantmodel', args=[self.pk])

class AzureSubscriptionModel(NetBoxModel):
    """Azure Subscription Model
    """
    subid = models.CharField(
        max_length=50
    )
    name = models.CharField(
        max_length=50
    )
    comment = models.TextField(
        blank=True
    )
    status = models.CharField(
        max_length=25,
        choices=choices.SubscriptionStatusChoices,
        default=choices.SubscriptionStatusChoices.STATUS_ACTIVE
    )
    approver = models.CharField(
        max_length=50
    )
    owner = models.CharField(
        max_length=50
    )
    tenant = models.ForeignKey(
        to=AzureTenantModel,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )

    class Meta:
        """Meta data for the AzureSubscriptionModel
        """
        ordering = ('name',)
        unique_together = ('tenant', 'subid')

    def __str__(self):
        return f'{self.name} ({self.subid})'

    def get_status_color(self):
        """Return the color associated with the status
        """
        return choices.SubscriptionStatusChoices.colors.get(self.status)

    def get_absolute_url(self):
        """Return the URL to access a particular instance of the model
        """
        return reverse('plugins:netbox_azure:azuresubscriptionmodel', args=[self.pk])
