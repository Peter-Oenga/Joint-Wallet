from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'full_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number', 'full_name')
    list_filter = ('is_staff', 'is_superuser')
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
