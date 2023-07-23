from django.urls import path
from . views import *

urlpatterns=[
    path('',home,name='home'),
    path('signin',signIn,name='sigin'),
    path('signup',signUp,name='signup'),
    path('logout',logoutUser,name='logout'),
    path('<str:name>',companies,name='company'),
    path('<str:name>/<int:year>',experience,name='experience'),
]