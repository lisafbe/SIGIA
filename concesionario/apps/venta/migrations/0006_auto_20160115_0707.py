# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_auto_20160115_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='sucursal_vehiculo',
            field=models.ForeignKey(to='sucursal.SucursalVehiculo', null=True),
        ),
    ]
