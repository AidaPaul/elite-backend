# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


def add_sidewinder(apps, schema_editor):
    Ship = apps.get_model('api', 'Ship')
    ShipType = apps.get_model('api', 'ShipType')
    ShipSlot = apps.get_model('api', 'ShipSlot')
    ShipParameter = apps.get_model('api', 'ShipParameter')
    ShipParameterType = apps.get_model('api', 'ShipParameterType')
    ModuleType = apps.get_model('api', 'ModuleType')
    ModuleParameter = apps.get_model('api', 'ModuleParameter')
    ModuleParameterType = apps.get_model('api', 'ModuleParameterType')
    ship = {
        'name': 'Sidewinder Mk. I',
        'type': 'Multipurpose',
        'parameters': {
            'base_price': 32000,
            'base_insurance': 1600,
            'top_speed': 220,
            'boost_speed': 320,
            'manouverability': 8,
            'shields': 40,
            'armour': 60,
            'base_mass': 25,
            'base_cargo': 4,
            'base_fuel': 2,
            'base_jump_range': 7.79,
            'size': 's',
            'fuel_cost': 50,
        },
        'slots': [
            {'type': 'hardpoint', 'size': 1},
            {'type': 'hardpoint', 'size': 1},
            {'type': 'utility mount', 'size': 0},
            {'type': 'utility mount', 'size': 0},
            {'type': 'bulkheads', 'size': 8},
            {'type': 'reactor bay', 'size': 2},
            {'type': 'thruster mounting', 'size': 2},
            {'type': 'frame shift drive housing', 'size': 2},
            {'type': 'environment control', 'size': 1},
            {'type': 'power coupling', 'size': 1},
            {'type': 'sensor suite', 'size': 1},
            {'type': 'fuel store', 'size': 1},
            {'type': 'internal compartment', 'size': 2},
            {'type': 'internal compartment', 'size': 2},
            {'type': 'internal compartment', 'size': 1},
        ]
    }
    sidewinder = Ship.objects.create(name=ship['name'], type=ShipType.objects.get(name=ship['type']))
    sidewinder.save()
    for parameter, value in ship['parameters'].items():
        parameter_type = ShipParameterType.objects.get(name=parameter)
        sidewinder.parameters.add(ShipParameter.objects.create(type=parameter_type, value=value))

    for slot in ship['slots']:
        slot_type = ModuleType.objects.get(name=slot['type'])
        slot_size = ModuleParameter.objects.create(type=ModuleParameterType.objects.get(name='size'), value=1)
        sidewinder.slots.add(ShipSlot.objects.create(type=slot_type, size=slot_size))


class Migration(migrations.Migration):
    dependencies = [
        ('api', 'ship_components'),
    ]

    operations = [
        migrations.RunPython(add_sidewinder),
    ]