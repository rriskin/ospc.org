# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-22 21:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid
import webapp.apps.btax.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BTaxOutputUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pk', models.IntegerField(default=None, null=True)),
                ('exp_comp_datetime', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('btax_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('taxcalc_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('webapp_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BTaxSaveInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btax_betr_corp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_betr_entity_Switch', models.NullBooleanField(default=None)),
                ('btax_betr_pass', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_allyr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_3yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_5yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_7yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_10yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_15yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_20yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_25yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_27_5yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_39yr', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('btax_depr_allyr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_3yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_5yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_7yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_10yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_15yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_20yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_25yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_27_5yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_39yr_gds_Switch', models.CharField(blank=True, default='True', max_length=50, null=True)),
                ('btax_depr_allyr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_3yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_5yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_7yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_10yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_15yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_20yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_25yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_27_5yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_39yr_ads_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_allyr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_3yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_5yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_7yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_10yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_15yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_20yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_25yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_27_5yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_39yr_tax_Switch', models.CharField(blank=True, default='False', max_length=50, null=True)),
                ('btax_depr_allyr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_3yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_5yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_7yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_10yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_15yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_20yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_25yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_27_5yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_depr_39yr_exp', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_other_hair', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_other_corpeq', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_other_proptx', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_other_invest', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_econ_nomint', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('btax_econ_inflat', webapp.apps.btax.models.CommaSeparatedField(blank=True, default=None, max_length=200, null=True)),
                ('job_id', models.UUIDField(blank=True, default=None, null=True)),
                ('first_year', models.IntegerField(default=None, null=True)),
                ('data_source', models.CharField(blank=True, default='PUF', max_length=20, null=True)),
                ('tax_result', models.TextField(blank=True, default=None, null=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
            ],
            options={
                'permissions': (('view_inputs', 'Allowed to view Taxbrain.'),),
            },
        ),
        migrations.AddField(
            model_name='btaxoutputurl',
            name='unique_inputs',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='btax.BTaxSaveInputs'),
        ),
        migrations.AddField(
            model_name='btaxoutputurl',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
