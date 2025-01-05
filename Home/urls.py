# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('book_appointment/<int:school_registration_id>/', views.book_appointment, name='book_appointment'),
    path('success/', views.success_view, name='success'),

]
