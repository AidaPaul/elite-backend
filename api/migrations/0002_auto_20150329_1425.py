# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllegianceRank',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=25)),
                ('allegiance', models.ForeignKey(to='api.Allegiance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleParameter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('value', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleParameterType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipParameter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('value', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipParameterType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipSlot',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('module', models.ForeignKey(null=True, to='api.Module')),
                ('size', models.ForeignKey(null=True, to='api.ModuleParameter')),
                ('type', models.ForeignKey(to='api.ModuleType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shipparameter',
            name='type',
            field=models.ForeignKey(to='api.ShipParameterType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='parameters',
            field=models.ManyToManyField(to='api.ShipParameter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='required_rank',
            field=models.ForeignKey(null=True, to='api.AllegianceRank'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='slots',
            field=models.ManyToManyField(to='api.ShipSlot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='type',
            field=models.ForeignKey(to='api.ShipType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moduleparameter',
            name='type',
            field=models.ForeignKey(to='api.ModuleParameterType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='parameters',
            field=models.ManyToManyField(to='api.ModuleParameter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='type',
            field=models.ForeignKey(to='api.ModuleType'),
            preserve_default=True,
        ),
    ]
