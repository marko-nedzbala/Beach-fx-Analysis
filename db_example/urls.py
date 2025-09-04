from django.urls import path

from . import views

app_name = 'db_example'

urlpatterns = [
    path('', views.default, name='default'),
]
