from django.contrib import admin
from .models import UserEmail

@admin.register(UserEmail)
class UserEmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
