from django.urls import path
from app2.views import *
app2='what1'
urlpatterns=[
    path('four/',four,name='four'),
    path('five/',five,name='five'),
]