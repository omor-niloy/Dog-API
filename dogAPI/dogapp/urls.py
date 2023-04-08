from django.urls import path
from dogapp import views

urlpatterns = [
    path('DOG/', views.api_list),
    path('Breed/', views.api_listB),
    path('apidetails/<int:pk>/', views.api_detail),
] 