from django.urls import path
from .views import check_email, get_modal_content, manage_modal_content  # Ensure all imports are correct

urlpatterns = [
    path('api/check-email/', check_email, name='check_email'),
    path('api/modal-content/', get_modal_content, name='modal-content'),
    path('manage-modal-content/', manage_modal_content, name='manage_modal_content'),  # Ensure this path is correct
]
