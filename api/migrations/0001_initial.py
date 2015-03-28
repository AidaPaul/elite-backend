# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allegiance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('average_price', models.IntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(to='api.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('supply', models.IntegerField()),
                ('demand', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('collected_at', models.DateTimeField()),
                ('update_count', models.IntegerField()),
                ('commodity', models.ForeignKey(to='api.Commodity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_landing_pad_size', models.CharField(null=True, max_length=1)),
                ('distance_to_star', models.IntegerField(null=True)),
                ('has_blackmarket', models.IntegerField()),
                ('has_commodities', models.IntegerField()),
                ('has_refuel', models.IntegerField()),
                ('has_repair', models.IntegerField()),
                ('has_rearm', models.IntegerField()),
                ('has_outfitting', models.IntegerField()),
                ('has_shipyard', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('allegiance', models.ForeignKey(null=True, to='api.Allegiance')),
                ('economies', models.ManyToManyField(to='api.Economy')),
                ('faction', models.ForeignKey(null=True, to='api.Faction')),
                ('government', models.ForeignKey(null=True, to='api.Government')),
                ('prohibited_commodities', models.ManyToManyField(to='api.Commodity')),
                ('state', models.ForeignKey(null=True, to='api.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StationType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('population', models.CharField(null=True, max_length=255)),
                ('needs_permit', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField()),
                ('allegiance', models.ForeignKey(null=True, to='api.Allegiance')),
                ('faction', models.ForeignKey(null=True, to='api.Faction')),
                ('government', models.ForeignKey(null=True, to='api.Government')),
                ('primary_economy', models.ForeignKey(null=True, to='api.Economy')),
                ('security', models.ForeignKey(null=True, to='api.Security')),
                ('state', models.ForeignKey(null=True, to='api.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(to='api.System'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='station',
            name='type',
            field=models.ForeignKey(null=True, to='api.StationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='station',
            field=models.ForeignKey(to='api.Station'),
            preserve_default=True,
        ),
    ]
