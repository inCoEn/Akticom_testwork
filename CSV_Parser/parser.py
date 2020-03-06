def change_value(val):

    if val:
        return val
    else:
        return None


class DictParser:

    def __init__(self, csv_dict):
        self.code = change_value(csv_dict['Код'])
        self.name = change_value(csv_dict['Наименование'])
        self.lvl_1 = change_value(csv_dict['Уровень1'])
        self.lvl_2 = change_value(csv_dict['Уровень2'])
        self.lvl_3 = change_value(csv_dict['Уровень3'])
        self.price = change_value(csv_dict['Цена'])
        if self.price:
            self.price = self.price.replace(',', '.')
        self.priceSP = change_value(csv_dict['ЦенаСП'])
        if self.priceSP:
            self.priceSP = self.priceSP.replace(',', '.')
        self.quantity = change_value(csv_dict['Количество'])
        self.prop = change_value(csv_dict['Поля свойств'])
        self.joint = change_value(csv_dict['Совместные покупки'])
        self.unit = change_value(csv_dict['Единица измерения'])
        self.pic = change_value(csv_dict['Картинка'])
        if csv_dict['Выводить на главной'] == '1':
            self.switcher = True
        else:
            self.switcher = False
        self.description = change_value(csv_dict['Описание'])

    def __str__(self):
        return 'Код: {}\nНаименование: {}\nУровень1: {}\nУровень2: {}\nУровень3: {}\n' \
               'Цена: {}\nЦенаСП: {}\nКоличество: {}\nСвойства: {}\nСовместные покупки: {}\n' \
               'Единица измерения: {}\nКартинка: {}\nНа главной: {}\n' \
               'Описание: {}\n'.format(self.code, self.name, self.lvl_1, self.lvl_2,
                                       self.lvl_3, self.price, self.priceSP, self.quantity,
                                       self.prop, self.joint, self.unit,
                                       self.pic, self.switcher, self.description)
