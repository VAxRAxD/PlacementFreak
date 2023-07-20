from django.urls import path
from . views import *

urlpatterns=[
    path('',home,name='home'),
    path('<str:year>/',companies,name='company'),
    path('<str:year>/<str:company>',experience,name='experience'),
    path('signin',signIn,name='sigin'),
    path('logout',logoutUser,name='logout')
]