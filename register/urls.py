from django.urls import path
from register import views

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('create/', views.registration_create, name='registration_create'),
    path('update/<int:pk>/', views.registration_update, name='registration_update'),
    path('delete/<int:pk>/', views.registration_delete, name='registration_delete'),
]