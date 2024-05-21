from django.urls import path

from Mer import views

urlpatterns = [
    path('', views.index, name='index'),
]