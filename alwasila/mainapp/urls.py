from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.plug, name='plug'),
    path('index/', views.index, name='index'),
]