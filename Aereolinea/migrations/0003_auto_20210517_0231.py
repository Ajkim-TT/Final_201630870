# Generated by Django 3.1 on 2021-05-17 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aereolinea', '0002_vuelofactura_cajero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelofactura',
            name='cajero',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
