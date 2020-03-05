from django.urls import re_path
from CSV_Parser.views import upload

urlpatterns = [
    re_path(r'^$', upload, name='upload_view')
]