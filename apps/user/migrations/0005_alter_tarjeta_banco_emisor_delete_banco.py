# Generated by Django 4.2.4 on 2023-11-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_banco_banco_alter_tarjeta_banco_emisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='banco_emisor',
            field=models.CharField(choices=[('BNA', 'Nacion Argentina'), ('Macro', 'Macro'), ('Galicia', 'Galicia'), ('Santander Rio', 'Santander Rio'), ('BBVA Argentina', 'Bbva Argentina'), ('Hipotecario', 'Hipotecario'), ('Ciudad', 'Ciudad'), ('Itau Argentina', 'Itau Argentina'), ('Patagonia', 'Patagonia'), ('Columbia', 'Columbia')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Banco',
        ),
    ]
