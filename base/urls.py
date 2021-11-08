from django.urls import path
from . import views


urlpatterns = [
    path('', views.ytb_down),
    path('download/',views.ytb_downloader),
]
