from django.urls import path
from dogapp import views

urlpatterns = [
    path('dogs/', views.AllDog.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', views.SingleDog.as_view(), name='dog-detail'),
    path('breeds/', views.AllBreed.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', views.SingleBreed.as_view(), name='breed-detail'),

] 