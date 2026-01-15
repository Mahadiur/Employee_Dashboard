from django.urls import path
from . import views

urlpatterns = [
    path('<int:primarykey>/', views.onlinebatchteam)
]