from django.urls import path
from . import views

urlpatterns = [
    path("<name>/<lang>", views.nomanpage, name="nomanpage"),
]
