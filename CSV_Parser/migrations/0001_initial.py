# Generated by Django 3.0.3 on 2020-03-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'Category_1',
            },
        ),
        migrations.CreateModel(
            name='SecondLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'Category_2',
            },
        ),
        migrations.CreateModel(
            name='ThirdLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'Category_3',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'Units',
            },
        ),
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Код')),
                ('name', models.TextField(verbose_name='Наименование')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('priceSP', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='ЦенаСП')),
                ('quantity', models.FloatField(verbose_name='Количество')),
                ('properties', models.TextField(null=True, verbose_name='Поля свойств')),
                ('joint_purchase', models.IntegerField(null=True, verbose_name='Совместные закупки')),
                ('pic', models.CharField(max_length=50, null=True, verbose_name='Картинка')),
                ('mainpage_switcher', models.BooleanField(verbose_name='Выводить на главной')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('lvl_1', models.ForeignKey(on_delete=models.SET('DELETED_CATEGORY'), to='CSV_Parser.FirstLevel', verbose_name='Уровень 1')),
                ('lvl_2', models.ForeignKey(on_delete=models.SET('DELETED_CATEGORY'), to='CSV_Parser.SecondLevel', verbose_name='Уровень 2')),
                ('lvl_3', models.ForeignKey(on_delete=models.SET('DELETED_CATEGORY'), to='CSV_Parser.ThirdLevel', verbose_name='Уровень 3')),
                ('unit', models.ForeignKey(on_delete=models.SET('DELETED_UNIT'), to='CSV_Parser.Units', verbose_name='Единица измерения')),
            ],
            options={
                'db_table': 'MainModel',
                'ordering': ['code', 'name'],
            },
        ),
    ]
