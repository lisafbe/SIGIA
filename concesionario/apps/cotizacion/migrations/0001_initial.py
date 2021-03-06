# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_habilitado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True, null=True)),
                ('fecha_vencimiento', models.DateField(null=True, blank=True)),
                ('forma_pago', models.CharField(default=b'Efectivo', max_length=20, choices=[(b'Credito', b'Credito'), (b'Efectivo', b'Efectivo'), (b'Tarjeta_credito', b'Tarjeta de credito'), (b'Tarjeta_debito', b'Tarjeta de debito')])),
                ('habilitado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
    ]
