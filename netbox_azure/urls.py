#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the urls' patterns for the netbox_azure app"""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from netbox_azure import models, views

urlpatterns = (
    #####################################################################################
    ### Azure Tenants
    path("tenants/", views.AzureTenantListView.as_view(), name="azuretenantmodel_list"),
    path(
        "tenants/add/", views.AzureTenantEditView.as_view(), name="azuretenantmodel_add"
    ),
    path("tenants/<int:pk>/", views.AzureTenantView.as_view(), name="azuretenantmodel"),
    path(
        "tenants/<int:pk>/edit/",
        views.AzureTenantEditView.as_view(),
        name="azuretenantmodel_edit",
    ),
    path(
        "tenants/<int:pk>/delete/",
        views.AzureTenantDeleteView.as_view(),
        name="azuretenantmodel_delete",
    ),
    path(
        "tenants/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="azuretenantmodel_changelog",
        kwargs={"model": models.AzureTenantModel},
    ),
    #####################################################################################
    ### Azure Subscriptions
    path(
        "subscriptions/",
        views.AzureSubscriptionListView.as_view(),
        name="azuresubscriptionmodel_list",
    ),
    path(
        "subscriptions/add/",
        views.AzureSubscriptionEditView.as_view(),
        name="azuresubscriptionmodel_add",
    ),
    path(
        "subscriptions/<int:pk>/",
        views.AzureSubscriptionView.as_view(),
        name="azuresubscriptionmodel",
    ),
    path(
        "subscriptions/<int:pk>/edit/",
        views.AzureSubscriptionEditView.as_view(),
        name="azuresubscriptionmodel_edit",
    ),
    path(
        "subscriptions/<int:pk>/delete/",
        views.AzureSubscriptionDeleteView.as_view(),
        name="azuresubscriptionmodel_delete",
    ),
    path(
        "subscriptions/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="azuresubscriptionmodel_changelog",
        kwargs={"model": models.AzureSubscriptionModel},
    ),
)
