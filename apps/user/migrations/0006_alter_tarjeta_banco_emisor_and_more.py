# Generated by Django 4.2.4 on 2023-11-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_tarjeta_banco_emisor_delete_banco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='banco_emisor',
            field=models.CharField(choices=[('BNA', 'Nacion Argentina'), ('Macro', 'Macro'), ('Galicia', 'Galicia'), ('Santander Rio', 'Santander Rio'), ('BBVA Argentina', 'Bbva Argentina'), ('Hipotecario', 'Hipotecario'), ('Ciudad', 'Ciudad'), ('Itau Argentina', 'Itau Argentina'), ('Patagonia', 'Patagonia'), ('Columbia', 'Columbia'), ("[('BNA', 'Banco de la Nación Argentina (BNA)'), ('Macro', 'Banco Macro'), ('Galicia', 'Banco Galicia'), ('Santander Rio', 'Banco Santander Río'), ('BBVA Argentina', 'Banco BBVA Argentina'), ('Hipotecario', 'Banco Hipotecario'), ('Ciudad', 'Banco Ciudad'), ('Itau Argentina', 'Banco Itaú Argentina'), ('Patagonia', 'Banco Patagonia'), ('Columbia', 'Banco Columbia')]", 'Bancos Choices')], max_length=365),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='tipo_tarjeta',
            field=models.CharField(choices=[('Visa', 'Visa'), ('MasterCard', 'Mastercard'), ('American Express', 'American Express'), ('Tarjeta Naranja', 'Tarjeta Naranja'), ('Tarjeta Shopping', 'Tarjeta Shopping'), ('Cabal', 'Cabal'), ('Maestro', 'Maestro'), ('Argencard', 'Argencard')], max_length=365),
        ),
    ]
