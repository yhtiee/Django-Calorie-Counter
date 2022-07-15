from django.urls import path, re_path
from . import views
urlpatterns = [

    path("", views.Virtual_page),
    path("landingpage", views.Landingpage, name = "landingpage")

]