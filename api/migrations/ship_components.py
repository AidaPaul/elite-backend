# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


def ship_types(apps, schema_editor):
    ShipType = apps.get_model('api', 'ShipType')
    types = ['Multipurpose', 'Combat', 'Freighter', 'Explorer', 'Passenger']
    for ship_type in types:
        ShipType.objects.create(name=ship_type)


def ship_parameter_types(apps, schema_editor):
    ShipParameterType = apps.get_model('api', 'ShipParameterType')
    types = ['base_price', 'base_insurance', 'top_speed', 'boost_speed', 'manouverability', 'shields', 'armour',
             'base_mass', 'base_cargo', 'base_fuel', 'base_jump_range', 'size', 'fuel_cost']
    for ship_parameter_type in types:
        ShipParameterType.objects.create(name=ship_parameter_type)


def module_types(apps, schema_editor):
    ModuleType = apps.get_model('api', 'ModuleType')
    types = ['hardpoint', 'utility mount', 'bulkheads', 'reactor bay', 'thruster mounting',
             'frame shift drive housing', 'environment control', 'power coupling', 'sensor suite', 'fuel store',
             'internal compartment']
    for module_type in types:
        ModuleType.objects.create(name=module_type)


def module_parameter_types(apps, schema_editor):
    ModuleParameterType = apps.get_model('api', 'ModuleParameterType')
    types = ['size', 'rating', 'base_price', 'mass', 'power_change', 'mount_type']
    for module_parameter_type in types:
        ModuleParameterType.objects.create(name=module_parameter_type)


def basic_modules(apps, schema_editor):
    Module = apps.get_model('api', 'Module')
    ModuleType = apps.get_model('api', 'ModuleType')
    ModuleParameter = apps.get_model('api', 'ModuleParameter')
    ModuleParameterType = apps.get_model('api', 'ModuleParameterType')

    modules = (
        {
            'name': 'pulse Laser',
            'type': 'hardpoint',
            'parameters': {
                'size': 1,
                'rating': 'f',
                'base_price': 2200,
                'mass': 2,
                'power_change': -0.39,
                'mount_type': 'fixed',
            }
        },
        {
            'name': 'lightweight alloy',
            'type': 'bulkheads',
            'parameters': {
                'size': 1,
                'rating': 'i',
                'base_price': 0,
                'mass': 0,
            }
        },
        {
            'name': 'power plant',
            'type': 'reactor bay',
            'parameters': {
                'size': 2,
                'rating': 'e',
                'base_price': 1978,
                'mass': 2.5,
                'power_change': +6.4,
            }
        },
        {
            'name': 'thrusters',
            'type': 'thruster mounting',
            'parameters': {
                'size': 2,
                'rating': 'e',
                'base_price': 1978,
                'mass': 2.5,
                'power_change': -2,
            }
        },
        {
            'name': 'frame shift drive',
            'type': 'frame shift drive housing',
            'parameters': {
                'size': 2,
                'rating': 'e',
                'base_price': 1978,
                'mass': 2.5,
                'power_change': -0.16,
            }
        },
        {
            'name': 'life support',
            'type': 'environment control',
            'parameters': {
                'size': 1,
                'rating': 'e',
                'base_price': 517,
                'mass': 1.3,
                'power_change': -0.32,
            }
        },
        {
            'name': 'power distributor',
            'type': 'power coupling',
            'parameters': {
                'size': 1,
                'rating': 'e',
                'base_price': 517,
                'mass': 1.3,
                'power_change': -0.32,
            }
        },
        {
            'name': 'sensors',
            'type': 'sensor suite',
            'parameters': {
                'size': 1,
                'rating': 'e',
                'base_price': 517,
                'mass': 1.3,
                'power_change': -0.32,
            }
        },
        {
            'name': 'fuel tank (capacity: 2)',
            'type': 'fuel store',
            'parameters': {
                'size': 1,
                'rating': 'c',
                'base_price': 1000,
                'mass': 2,
            }
        },
        {
            'name': 'shield generator',
            'type': 'internal compartment',
            'parameters': {
                'size': 2,
                'rating': 'e',
                'base_price': 1978,
                'mass': 2.5,
                'power_change': -0.9,
            }
        },
        {
            'name': 'cargo rack (capacity: 4)',
            'type': 'internal compartment',
            'parameters': {
                'size': 2,
                'rating': 'e',
                'base_price': 3250,
            }
        },
        {
            'name': 'basic discovery scanner',
            'type': 'internal compartment',
            'parameters': {
                'size': 1,
                'rating': 'e',
                'base_price': 1000,
                'mass': 2,
            }
        },
    )

    for module in modules:
        new_module = Module.objects.create(name=module['name'],
                                           type=ModuleType.objects.get_or_create(name=module['type'])[0])
        new_module.save()
        for name, value in module['parameters'].items():
            parameter_type = ModuleParameterType.objects.get_or_create(name=name)[0]
            new_module.parameters.add(ModuleParameter.objects.create(value=value, type=parameter_type))


class Migration(migrations.Migration):
    dependencies = [
        ('api', 'allegiances_and_ranks'),
    ]

    operations = [
        migrations.RunPython(module_types),
        migrations.RunPython(module_parameter_types),
        migrations.RunPython(basic_modules),
        migrations.RunPython(ship_types),
        migrations.RunPython(ship_parameter_types),
    ]
