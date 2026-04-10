from django.urls import path
from . import views
import myapplication


urlpatterns=[path('',views.index,name='index'),path('<int:animal_id>', views.one_zoo,name='one_zoo')]