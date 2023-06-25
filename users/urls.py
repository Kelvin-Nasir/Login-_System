from django.urls import path
from .views import home, profile, RegisterView, RegisterAPIView 

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('register-api/', RegisterAPIView.as_view(), name='users-register-api'),  # API endpoint
    path('profile/', profile, name='users-profile'),
]

