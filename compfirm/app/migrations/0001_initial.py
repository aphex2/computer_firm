# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data.json')


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('code', models.AutoField(serialize=False, primary_key=True)),
                ('speed', models.SmallIntegerField()),
                ('ram', models.SmallIntegerField()),
                ('hd', models.FloatField()),
                ('price', models.DecimalField(null=True, max_digits=12, decimal_places=2)),
                ('screen', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('code', models.AutoField(serialize=False, primary_key=True)),
                ('speed', models.SmallIntegerField()),
                ('ram', models.SmallIntegerField()),
                ('hd', models.FloatField()),
                ('cd', models.CharField(max_length=10)),
                ('price', models.DecimalField(null=True, max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('code', models.AutoField(serialize=False, primary_key=True)),
                ('color', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=10)),
                ('price', models.DecimalField(null=True, max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('maker', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='printer',
            name='model',
            field=models.ForeignKey(to='app.Product'),
        ),
        migrations.AddField(
            model_name='pc',
            name='model',
            field=models.ForeignKey(to='app.Product'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='model',
            field=models.ForeignKey(to='app.Product'),
        ),
        migrations.RunPython(load_fixture),
    ]
