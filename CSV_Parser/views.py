import os
import csv
import traceback
from django.shortcuts import render
from django.db.utils import IntegrityError
from Akticom_testwork.settings import BASE_DIR
from CSV_Parser.forms import UploadFileForm
from CSV_Parser.parser import DictParser
from CSV_Parser.models import MainModel, FirstLevel, SecondLevel, ThirdLevel, Units

data_bulk = []


def upload_file_handler(file):
    """
    Uploading file to server
    :param file: request.FILES object
    :return: path to uploaded file
    """

    with open(os.path.join(BASE_DIR, r'Media\temp', file.name), 'wb+') as tmp_file:
        for chunk in file.chunks():
            tmp_file.write(chunk)
        return os.path.join(BASE_DIR, r'Media\temp', file.name)


def add_to_bulk(parser):
    """
    Func append MainModel object to global list
    :param parser: DictParser
    :return: None
    """

    global data_bulk

    if type(parser) == DictParser:
        data_bulk.append(MainModel(code=parser.code,
                                   name=parser.name,
                                   lvl_1=FirstLevel.objects.get_or_create(name=parser.lvl_1)[0],
                                   lvl_2=SecondLevel.objects.get_or_create(name=parser.lvl_2)[0],
                                   lvl_3=ThirdLevel.objects.get_or_create(name=parser.lvl_3)[0],
                                   price=parser.price,
                                   priceSP=parser.priceSP,
                                   quantity=parser.quantity,
                                   properties=parser.prop,
                                   joint_purchase=parser.joint,
                                   unit=Units.objects.get_or_create(unit=parser.unit)[0],
                                   pic=parser.pic,
                                   mainpage_switcher=parser.switcher,
                                   description=parser.description))


def update_db(bulk_list):
    """
    Func run bulk_create with list of MainModel objects.
    In case of exceptions function is run recursively
    with half of list
    :param bulk_list: list of MainModel objects
    :return: None
    """

    if len(bulk_list) > 1:
        try:
            MainModel.objects.bulk_create(bulk_list)
        except (ValueError, IntegrityError):
            half = len(bulk_list)
            bulks_list = [bulk_list[:half], bulk_list[half:]]
            for item in bulks_list:
                update_db(item)
    if len(bulk_list) == 1:
        try:
            bulk_list[0].save()
        except (ValueError, IntegrityError):
            print(bulk_list[0])
            print(traceback.format_exc())
    else:
        pass


def upload(request):

    global data_bulk

    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST)
        if upload_form.is_valid():
            if request.FILES.get('csv_file', False):
                tmp_file = upload_file_handler(request.FILES['csv_file'])

                with open(tmp_file, 'r', encoding='cp1251', errors='ignore') as csv_file:
                    data_dict = []
                    csv_dict = csv.DictReader(csv_file, delimiter=';')

                    for item in csv_dict:
                        data_dict.append(item)
                for item in data_dict:

                    parser = DictParser(item)
                    add_to_bulk(parser)
                    if len(data_bulk) >= 500:
                        update_db(data_bulk)
                        data_bulk = []
                if len(data_bulk) != 0:
                    update_db(data_bulk)
                    data_bulk = []
                return render(request, 'upload_page.html', {'upload_form': upload_form,
                                                            'message': 'DB was updated'})
            else:
                upload_form = UploadFileForm(request.POST)
                return render(request, 'upload_page.html', {'upload_form': upload_form,
                                                            'message': 'No file in form'})
        else:
            upload_form = UploadFileForm(request.POST)
            return render(request, 'upload_page.html', {'upload_form': upload_form,
                                                        'message': 'Invalid form'})
    else:
        upload_form = UploadFileForm(request.POST)
        return render(request, 'upload_page.html', {'upload_form': upload_form})
