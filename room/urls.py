from django.contrib.auth import views as auth_views
from django import views
from room import views
from django.urls import path
urlpatterns = [

    path('',views.rooms,name='rooms'),
    path('<slug:slug>/',views.room,name='room'), 

]