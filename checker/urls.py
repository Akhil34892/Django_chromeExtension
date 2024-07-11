from django.urls import path
from .views import check_email

urlpatterns = [
    path('api/check-email/', check_email, name='check_email'),
]
