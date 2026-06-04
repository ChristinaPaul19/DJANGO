from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'), 
    path('contacts/', views.contacts, name='contacts'),
    path('Book/', views.Book, name='Book'),
    path('view_books/', views.viewBooks, name='view_books'),
    ]
