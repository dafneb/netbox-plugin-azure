#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the forms for the netbox_azure app
"""

from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from netbox_azure import models, choices

class AzureTenantForm(NetBoxModelForm):
    """Form for the AzureTenantModel
    """
    comment = CommentField()

    class Meta:
        """Meta data for the AzureTenantForm
        """
        model = models.AzureTenantModel
        fields = [
            'name',
            'tenid', 
            'comment',
            'tags',
        ]
        labels = {
            'name': 'Tenant Name',
            'tenid': 'Tenant ID',
            'comment': 'Comment',
        }

class AzureSubscriptionForm(NetBoxModelForm):
    """Form for the AzureSubscriptionModel
    """
    comment = CommentField()
    tenant = DynamicModelChoiceField(
        queryset=models.AzureTenantModel.objects.all()
    )

    class Meta:
        """Meta data for the AzureSubscriptionForm
        """
        model = models.AzureSubscriptionModel
        fields = [
            'name',
            'subid',
            'comment',
            'status',
            'approver',
            'owner',
            'tenant',
            'tags',
        ]
        labels = {
            'name': 'Subscription Name',
            'subid': 'Subscription ID',
            'comment': 'Comment',
            'status': 'Status',
            'approver': 'Approver',
            'owner': 'Owner',
            'tenant': 'Azure Tenant',
        }
        help_texts = {
            'tenant': 'The Azure Tenant to which this subscription belongs',
        }

class AzureSubscriptionFilterForm(NetBoxModelFilterSetForm):
    """Filter form for the AzureSubscriptionModel
    """
    model = models.AzureSubscriptionModel
    tenant = forms.ModelMultipleChoiceField(
        queryset=models.AzureTenantModel.objects.all(),
        required=False
    )
    status = forms.MultipleChoiceField(
        choices=choices.SubscriptionStatusChoices,
        required=False
    )
    approver = forms.CharField(
        required=False
    )
    owner = forms.CharField(
        required=False
    )
