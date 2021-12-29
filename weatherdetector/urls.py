from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name="index") #empty quotes because its the root url (main page)
]
