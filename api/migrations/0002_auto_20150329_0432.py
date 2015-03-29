# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactionRank',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('faction', models.ForeignKey(to='api.Faction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleParameter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleParameterType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('modules', models.ManyToManyField(to='api.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipParameter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipParameterType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=25)),
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
            field=models.ForeignKey(to='api.FactionRank'),
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
