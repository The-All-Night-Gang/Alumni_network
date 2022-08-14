from django.urls import path
from feed import views

urlpatterns = [
 
    path('feeds/', views.gallery, name='gallery'),
    path('event/', views.events, name='event'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]
