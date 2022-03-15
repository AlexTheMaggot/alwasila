from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('plug/', views.plug, name='plug'),
]