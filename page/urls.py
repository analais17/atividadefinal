from django.urls import path
from. import views

urlpatterns = [
    path('', views.log),
    path('home/', views.home)
]