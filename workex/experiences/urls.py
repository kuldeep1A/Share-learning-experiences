from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiences_list, name = 'experience_list'),
    path('<int:pk>/', views.experience_detail, name = 'experience_detail'),
]
