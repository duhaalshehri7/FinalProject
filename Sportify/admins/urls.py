from django.urls import path
from . import views

app_name = 'admins'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]