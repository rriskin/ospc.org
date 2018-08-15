# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-15 20:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid
import webapp.apps.btax.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxbrain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicElasticityOutputUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pk', models.IntegerField(default=None, null=True)),
                ('exp_comp_datetime', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('taxcalc_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('webapp_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicElasticitySaveInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source', models.CharField(blank=True, default='PUF', max_length=20, null=True)),
                ('elastic_gdp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('job_ids', webapp.apps.btax.models.SeparatedValuesField(blank=True, default=None, null=True)),
                ('jobs_not_ready', webapp.apps.btax.models.SeparatedValuesField(blank=True, default=None, null=True)),
                ('first_year', models.IntegerField(default=None, null=True)),
                ('tax_result', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('micro_run', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxbrain.TaxBrainRun')),
            ],
            options={
                'permissions': (('view_inputs', 'Allowed to view Taxbrain.'),),
            },
        ),
        migrations.CreateModel(
            name='DynamicOutputUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pk', models.IntegerField(default=None, null=True)),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('ogusa_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('webapp_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicSaveInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source', models.CharField(blank=True, default='PUF', max_length=20, null=True)),
                ('g_y_annual', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('g_y_annual_cpi', models.NullBooleanField(default=None)),
                ('upsilon', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('upsilon_cpi', models.NullBooleanField(default=None)),
                ('frisch', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('job_ids', webapp.apps.btax.models.SeparatedValuesField(blank=True, default=None, null=True)),
                ('guids', webapp.apps.btax.models.SeparatedValuesField(blank=True, default=None, null=True)),
                ('first_year', models.IntegerField(default=None, null=True)),
                ('tax_result', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('user_email', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('micro_run', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxbrain.TaxBrainRun')),
            ],
            options={
                'permissions': (('view_inputs', 'Allowed to view Taxbrain.'),),
            },
        ),
        migrations.CreateModel(
            name='OGUSAWorkerNodesCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singleton_enforce', models.IntegerField(default=1, unique=True)),
                ('current_idx', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='dynamicoutputurl',
            name='unique_inputs',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dynamic.DynamicSaveInputs'),
        ),
        migrations.AddField(
            model_name='dynamicoutputurl',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dynamicelasticityoutputurl',
            name='unique_inputs',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dynamic.DynamicElasticitySaveInputs'),
        ),
        migrations.AddField(
            model_name='dynamicelasticityoutputurl',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
