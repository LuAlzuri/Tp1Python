# Generated by Django 5.0 on 2023-12-07 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0003_categoria_cliente_metododecobro_metododepago_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='id',
            new_name='idCat',
        ),
        migrations.RenameField(
            model_name='metododepago',
            old_name='idCliente',
            new_name='idPago',
        ),
        migrations.AddField(
            model_name='metododecobro',
            name='idServicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prueba.servicio'),
        ),
        migrations.AddField(
            model_name='metododecobro',
            name='tipoMet',
            field=models.CharField(default=1, max_length=30),
        ),
        migrations.AddField(
            model_name='metododepago',
            name='tipoMetPag',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='idServicio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
