from django.urls import path, include
from .views import UserRegistrationView


app_name = 'users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
]
