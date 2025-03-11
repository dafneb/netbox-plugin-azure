#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the views for the netbox_azure app
"""

from django.shortcuts import render
from django.views.generic import View
from .models import AzureTenantModel, AzureSubscriptionModel
from .forms import AzureTenantForm, AzureSubscriptionForm
from .tables import AzureTenantTable, AzureSubscriptionTable
