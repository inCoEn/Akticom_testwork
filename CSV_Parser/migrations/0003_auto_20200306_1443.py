# Generated by Django 3.0.3 on 2020-03-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_Parser', '0002_auto_20200306_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmodel',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Код'),
        ),
    ]
