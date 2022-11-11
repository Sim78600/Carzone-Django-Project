from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('serv',views.serv,name='serv'),
    path('cont',views.contact,name='cont'),

]
