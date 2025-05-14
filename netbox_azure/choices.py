#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the choices for the netbox_azure app"""

from utilities.choices import ChoiceSet


class SubscriptionStatusChoices(ChoiceSet):
    """ChoiceSet for Azure Subscription Status"""

    key = "AzureSubscriptionModel.status"

    STATUS_ACTIVE = "active"
    STATUS_DELETED = "deleted"
    STATUS_DISABLED = "disabled"
    STATUS_EXPIRED = "expired"
    STATUS_PAST_DUE = "pastdue"
    STATUS_WARNED = "warned"

    CHOICES = [
        (STATUS_ACTIVE, "Active", "green"),
        (STATUS_DELETED, "Deleted", "red"),
        (STATUS_DISABLED, "Disabled", "red"),
        (STATUS_EXPIRED, "Expired", "red"),
        (STATUS_PAST_DUE, "Past Due", "orange"),
        (STATUS_WARNED, "Warned", "orange"),
    ]
