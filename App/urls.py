from django.urls import path
from . views import *

urlpatterns=[
    path('',home,name='home'),
    path('signin/',signIn,name='sigin'),
    path('signup/',signUp,name='signup'),
    path('logout/',logoutUser,name='logout'),
    path('comp/<str:name>/',companies,name='company'),
    path('exp/<str:name>/<int:year>/',experience,name='experience'),
    path('unver/exp/',unverified,name='unverified'),
    path('verify/<int:id>/',verify,name='verification'),
    path('exp_add/', exp_add, name="exp_add" ),
    path('exp_update/<int:pk>/', exp_update, name="exp_update" ),
    path('exp_delete/<int:pk>/', exp_delete, name="exp_delete" ),
]