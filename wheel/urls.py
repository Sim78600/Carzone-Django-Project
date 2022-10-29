from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('serv',views.serv,name='serv'),
    path('cont',views.cont,name='cont'),
    # path('about',views.about,name='about')
    # path('about',views.about,name='about')

]
