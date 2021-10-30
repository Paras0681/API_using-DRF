from django.urls import path
from django.urls.conf import include
from . views import RegisterUser, Homepage
urlpatterns = [
    path('', Homepage.as_view(), name='user_api'),
    path('register/', RegisterUser.as_view(), name='register'),
]
