# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-05 21:51


from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('btax', '0002_btaxoutputurl_webapp_vers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btaxoutputurl',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='btaxsaveinputs',
            name='tax_result',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
