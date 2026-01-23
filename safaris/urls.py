from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('safaris/', views.safari_packages, name='safari_packages'),
    path('places/', views.places, name='places'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
    path('packages/', views.packages, name='packages'),
    path('packages/<int:id>/',views.safari_detail, name='safari_detail'),
    path('contact/', views.contact, name='contact'),
]