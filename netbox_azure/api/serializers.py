#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the serializers for the netbox_azure app"""

from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from netbox_azure import models


class AzureTenantSerializer(NetBoxModelSerializer):
    """Serializer for the AzureTenantModel"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_azure-api:azuretenantmodel-detail"
    )

    class Meta:
        """Meta data for the AzureTenantSerializer"""

        model = models.AzureTenantModel
        fields = [
            "id",
            "display",
            "url",
            "tenid",
            "name",
            "comment",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        ]


class NestedAzureTenantSerializer(WritableNestedSerializer):
    """Nested Serializer for the AzureTenantModel"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_azure-api:azuretenantmodel-detail"
    )

    class Meta:
        """Meta data for the NestedAzureTenantSerializer"""

        model = models.AzureTenantModel
        fields = ("id", "url", "display", "name")


class AzureSubscriptionSerializer(NetBoxModelSerializer):
    """Serializer for the AzureSubscriptionModel"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_azure-api:azuresubscriptionmodel-detail"
    )
    tenant = NestedAzureTenantSerializer()

    class Meta:
        """Meta data for the AzureSubscriptionSerializer"""

        model = models.AzureSubscriptionModel
        fields = [
            "id",
            "display",
            "url",
            "subid",
            "name",
            "comment",
            "status",
            "approver",
            "owner",
            "tenant",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        ]


class NestedAzureSubscriptionSerializer(WritableNestedSerializer):
    """Nested Serializer for the AzureSubscriptionModel"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_azure-api:azuresubscriptionmodel-detail"
    )

    class Meta:
        """Meta data for the NestedAzureSubscriptionSerializer"""

        model = models.AzureSubscriptionModel
        fields = ("id", "url", "display", "name")
