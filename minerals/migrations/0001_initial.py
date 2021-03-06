# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-25 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image_filename', models.CharField(max_length=512)),
                ('image_caption', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('formula', models.CharField(max_length=1024)),
                ('strunz_classification', models.CharField(max_length=255)),
                ('crystal_system', models.CharField(max_length=255)),
                ('unit_cell', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('crystal_symmetry', models.CharField(max_length=255)),
                ('cleavage', models.CharField(max_length=255)),
                ('mohs_scale_hardness', models.CharField(max_length=255)),
                ('luster', models.CharField(max_length=255)),
                ('streak', models.CharField(max_length=255)),
                ('diaphaneity', models.CharField(max_length=255)),
                ('optical_properties', models.CharField(max_length=255)),
                ('refractive_index', models.CharField(max_length=255)),
                ('crystal_habit', models.CharField(max_length=255)),
                ('specific_gravity', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
