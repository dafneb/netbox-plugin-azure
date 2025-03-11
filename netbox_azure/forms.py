#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the forms for the netbox_azure app
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import AzureTenantModel, AzureSubscriptionModel

class AzureTenantForm(NetBoxModelForm):
    """Form for the AzureTenantModel
    """
    comment = CommentField()

    class Meta:
        """Meta data for the AzureTenantForm
        """
        model = AzureTenantModel
        fields = ['name', 'tenid', 'comment']
        labels = {
            'tenid': 'Tenant ID',
            'name': 'Tenant Name',
            'comment': 'Comment',
        }

class AzureSubscriptionForm(NetBoxModelForm):
    """Form for the AzureSubscriptionModel
    """
    comment = CommentField()
    tenant = DynamicModelChoiceField(
        queryset=AzureTenantModel.objects.all()
    )

    class Meta:
        """Meta data for the AzureSubscriptionForm
        """
        model = AzureSubscriptionModel
        fields = ['name', 'subid', 'comment', 'status', 'approver', 'owner', 'tenant']
        labels = {
            'tenant': 'Azure Tenant',
            'name': 'Subscription Name',
            'subid': 'Subscription ID',
            'comment': 'Comment',
            'status': 'Status',
            'approver': 'Approver',
            'owner': 'Owner',
        }
        help_texts = {
            'tenant': 'The Azure Tenant to which this subscription belongs',
        }
