# Generated by Django 4.2.4 on 2023-11-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_remove_direccion_calle_alter_persona_fechanacimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='calle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
