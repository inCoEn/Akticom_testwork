from django.urls import re_path, path
from CSV_Parser.views import upload, show_full_list

urlpatterns = [
    re_path(r'^$', upload, name='upload_view'),
    path('full_list/', show_full_list, name='full_list')
]