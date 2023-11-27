# Generated by Django 4.2.4 on 2023-11-27 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_alter_component_dimensions_and_more'),
        ('factura', '0002_alter_factura_empresa'),
        ('detalle', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to='factura.factura'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='producto.component'),
        ),
    ]