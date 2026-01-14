from django.urls import path
from . import views

urlpatterns=[
    path('<int>:primarykey', views.backenddev_details)
]