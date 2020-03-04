from django.db import models


class FirstLevel(models.Model):

    name = models.CharField(max_length=100,
                            unique=True)

    class Meta:
        db_table = 'Category_1'


class SecondLevel(models.Model):

    name = models.CharField(max_length=100,
                            unique=True,
                            null=True)

    class Meta:
        db_table = 'Category_2'


class ThirdLevel(models.Model):

    name = models.CharField(max_length=100,
                            unique=True,
                            null=True)

    class Meta:
        db_table = 'Category_3'


class Units(models.Model):

    unit = models.CharField(max_length=20,
                            unique=True,
                            null=True)

    class Meta:
        db_table = 'Units'


class MainModel(models.Model):

    code = models.CharField(max_length=50,
                            verbose_name='Код')
    name = models.TextField(verbose_name='Наименование')
    lvl_1 = models.ForeignKey(FirstLevel,
                              on_delete=models.SET('DELETED_CATEGORY'),
                              verbose_name='Уровень 1')
    lvl_2 = models.ForeignKey(SecondLevel,
                              on_delete=models.SET('DELETED_CATEGORY'),
                              verbose_name='Уровень 2')
    lvl_3 = models.ForeignKey(ThirdLevel,
                              on_delete=models.SET('DELETED_CATEGORY'),
                              verbose_name='Уровень 3')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=True,
                                verbose_name='Цена')
    priceSP = models.DecimalField(max_digits=10,
                                  decimal_places=2,
                                  null=True,
                                  verbose_name='ЦенаСП')
    quantity = models.FloatField(verbose_name='Количество')
    properties = models.TextField(verbose_name='Поля свойств',
                                  null=True)
    joint_purchase = models.IntegerField(null=True,
                                         verbose_name='Совместные закупки')
    unit = models.ForeignKey(Units,
                             on_delete=models.SET('DELETED_UNIT'),
                             verbose_name='Единица измерения')
    pic = models.CharField(max_length=50,
                           null=True,
                           verbose_name='Картинка')
    mainpage_switcher = models.BooleanField(verbose_name='Выводить на главной')
    description = models.TextField(null=True,
                                   verbose_name='Описание')

    class Meta:
        db_table = 'MainModel'
        ordering = ['code', 'name']

    def __str__(self):
        return 'Код: {}\nНаименование: {}\nУровень1: {}\nУровень2: {}\nУровень3: {}\n' \
               'Цена: {}\nЦенаСП: {}\nКоличество: {}\nСвойства: {}\nСовместные покупки: {}\n' \
               'Единица измерения: {}\nКартинка: {}\nНа главной: {}\n' \
               'Описание: {}\n'.format(self.code, self.name, self.lvl_1, self.lvl_2,
                                       self.lvl_3, self.price, self.priceSP, self.quantity,
                                       self.properties, self.joint_purchase, self.unit,
                                       self.pic, self.mainpage_switcher, self.description)
