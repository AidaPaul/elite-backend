# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def faction_ranks(apps, schema_editor):
    allegiancerank = apps.get_model('api', 'AllegianceRank')
    federation = apps.get_model('api', 'Allegiance').objects.create(name='Federation')
    ranks = ['Recruit', 'Cadet', 'Midshipman', 'Petty Officer', 'Chief Petty Officer', 'Warrant Officer', 'Ensign',
             'Lieutenant', 'Lieutenant Commander', 'Post Commander']
    for rank in ranks:
        allegiancerank.objects.get_or_create(name=rank, allegiance=federation)


def empire_ranks(apps, schema_editor):
    allegiancerank = apps.get_model('api', 'AllegianceRank')
    empire = apps.get_model('api', 'Allegiance').objects.create(name='Empire')
    ranks = ['Outsider', 'Serf', 'Master', 'Squire', 'Knight', 'Lord', 'Baron', 'Viscount', 'Count', 'Earl']
    for rank in ranks:
        allegiancerank.objects.get_or_create(name=rank, allegiance=empire)


def alliance(apps, schema_editor):
    apps.get_model('api', 'Allegiance').objects.create(name='Alliance')


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20150329_0515'),
    ]

    operations = [
        migrations.RunPython(faction_ranks),
        migrations.RunPython(empire_ranks),
        migrations.RunPython(alliance),
    ]
