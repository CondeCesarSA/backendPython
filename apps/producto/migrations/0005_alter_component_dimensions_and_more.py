# Generated by Django 4.2.4 on 2023-11-27 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_unitcapacitance_unitresistance_unitvolt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='dimensions',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='producto.dimensions'),
        ),
        migrations.AlterField(
            model_name='component',
            name='distributor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='distributor', to='producto.distributor'),
        ),
        migrations.AlterField(
            model_name='component',
            name='manufacturer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='producto.manufacturer'),
        ),
        migrations.AlterField(
            model_name='component',
            name='physical',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='physical', to='producto.physical'),
        ),
        migrations.AlterField(
            model_name='component',
            name='technical',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='technical', to='producto.technical'),
        ),
    ]
