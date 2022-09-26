from django.contrib import admin
from django.urls import path,include
from introduce import views

urlpatterns = [
    path('introduce/',views.Test),
]
