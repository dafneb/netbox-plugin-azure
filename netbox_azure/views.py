#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the views for the netbox_azure app
"""

from netbox.views import generic
from netbox_azure import models, forms, tables, filtersets

class AzureTenantView(generic.ObjectView):
    """This class is the view for the AzureTenantModel
    """
    queryset = models.AzureTenantModel.objects.all()

    def get_extra_context(self, request, instance):
        """Return the extra context for the view
        """
        table = tables.AzureSubscriptionTable(instance.subscriptions.all())
        table.configure(request)

        return {
            'subscriptions_table': table,
        }

class AzureTenantListView(generic.ObjectListView):
    """This class is the list view for the AzureTenantModel
    """
    queryset = models.AzureTenantModel.objects.all()
    table = tables.AzureTenantTable

class AzureTenantEditView(generic.ObjectEditView):
    """This class is the edit view for the AzureTenantModel
    """
    queryset = models.AzureTenantModel.objects.all()
    form = forms.AzureTenantForm

class AzureTenantDeleteView(generic.ObjectDeleteView):
    """This class is the delete view for the AzureTenantModel
    """
    queryset = models.AzureTenantModel.objects.all()

class AzureSubscriptionView(generic.ObjectView):
    """This class is the view for the AzureSubscriptionModel
    """
    queryset = models.AzureSubscriptionModel.objects.all()

class AzureSubscriptionListView(generic.ObjectListView):
    """This class is the list view for the AzureSubscriptionModel
    """
    queryset = models.AzureSubscriptionModel.objects.all()
    table = tables.AzureSubscriptionTable
    filterset = filtersets.AzureSubscriptionFilterSet
    filterset_form = forms.AzureSubscriptionFilterForm

class AzureSubscriptionEditView(generic.ObjectEditView):
    """This class is the edit view for the AzureSubscriptionModel
    """
    queryset = models.AzureSubscriptionModel.objects.all()
    form = forms.AzureSubscriptionForm

class AzureSubscriptionDeleteView(generic.ObjectDeleteView):
    """This class is the delete view for the AzureSubscriptionModel
    """
    queryset = models.AzureSubscriptionModel.objects.all()
