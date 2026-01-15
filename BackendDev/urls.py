from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>/', views.backenddev_details, name='backend')
]