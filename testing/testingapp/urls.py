from testingapp import views
from django.urls import path
import django.contrib.staticfiles

app_name = 'testingapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('pictures/',views.pictures,name='pictures'),
]
