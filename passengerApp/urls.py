from django.urls import path
from passengerApp import views

urlpatterns = [
    path('passengers/', views.passengers),
    path('passenger/<int:pk>', views.passenger)
]