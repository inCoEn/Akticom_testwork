# Generated by Django 3.0.3 on 2020-03-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_Parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmodel',
            name='quantity',
            field=models.FloatField(null=True, verbose_name='Количество'),
        ),
    ]
