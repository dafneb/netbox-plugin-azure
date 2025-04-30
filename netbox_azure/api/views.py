#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the serializers for the netbox_azure app
"""

from netbox.api.viewsets import NetBoxModelViewSet

from netbox_azure.api import serializers
from netbox_azure import models, filtersets

class AzureTenantViewSet(NetBoxModelViewSet):
    """This class is the viewset for the AzureTenantModel
    """

    queryset = models.AzureTenantModel.objects.prefetch_related(
        'tags'
    )
    serializer_class = serializers.AzureTenantSerializer

class AzureSubscriptionViewSet(NetBoxModelViewSet):
    """This class is the viewset for the AzureSubscriptionModel
    """

    queryset = models.AzureSubscriptionModel.objects.prefetch_related(
        'tenant'
        ,'tags'
    )
    serializer_class = serializers.AzureSubscriptionSerializer
    filterset_class = filtersets.AzureSubscriptionFilterSet
