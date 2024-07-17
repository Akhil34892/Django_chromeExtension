from django.contrib import admin
from .models import UserEmail, ModalContent
from .forms import ModalContentForm

@admin.register(UserEmail)
class UserEmailAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(ModalContent)
class ModalContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'video_url', 'video_file')
    form = ModalContentForm
