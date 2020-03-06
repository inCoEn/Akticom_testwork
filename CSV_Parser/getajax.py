import cgi
from django.shortcuts import render


def get_data(request):

    storage = cgi.FieldStorage()
    data = storage.getvalue('data')
    if data:
        print(data)
    else:
        print('NoDATA')

    return render(request, 'upload_page.html')
