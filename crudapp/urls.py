from django.urls import path , include
from django.views.generic import RedirectView
from . views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'myprofile',ProfileViewSet)
router.register(r'myuser',UserViewSet)

urlpatterns = [
    path('home/', Home),
    path('registers/', sign_up),
    path('signin/',sign_in),
    path('logout/',log_out),
    path('deleteProfile/<int:i_d>', DeleteProfile),
    path('editprofile/<int:pk>',ProfileUpdateView.as_view(success_url='/crudapp/home/')),
    path('viewprofile/<int:i_d>',view_profile),
    path(r'api/',include(router.urls)),
    path('',RedirectView.as_view(url="home/")),
]
