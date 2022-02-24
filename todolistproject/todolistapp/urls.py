from django.urls import path, include
from .views import helloAPI
from .views import *

urlpatterns = [
    path("hello/", helloAPI),
    path('', todolist, name='list'),
    path('create/', todocreate, name='create'),
    path('update/<str:pk>/', todoupdate, name='update'),
    path('delete/<str:pk>/', tododelete, name='delete'),
    # path('', taglist, name='list'),
    # path('create/', tagcreate, name='create'),
    # path('update/<str:pk>/', tagupdate, name='update'),
    # path('delete/<str:pk>/', tagdelete, name='delete')
]

