from django.urls import path
from app1.views import *
app1='what'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]