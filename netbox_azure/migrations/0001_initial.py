# Generated by Django 5.1.7 on 2025-03-13 16:33

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0122_charfield_null_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='AzureTenantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('tenid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=250)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AzureSubscriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('subid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=250)),
                ('status', models.CharField(default='active', max_length=25)),
                ('approver', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netbox_azure.azuretenantmodel')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
