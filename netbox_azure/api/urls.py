#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the urls' patterns for the netbox_azure app api
"""

from netbox.api.routers import NetBoxRouter
from netbox_azure.api import views

app_name = 'netbox_azure'

router = NetBoxRouter()
router.register('tenants', views.AzureTenantViewSet)
router.register('subscriptions', views.AzureSubscriptionViewSet)

urlpatterns = router.urls
