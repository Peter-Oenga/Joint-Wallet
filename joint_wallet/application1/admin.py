from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MonthlySaving, Fine, Transaction, Loan, Payment, CustomUser, BlogPost

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number', 'address')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('phone_number', 'address')}),
#     )


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MonthlySaving)
admin.site.register(Fine)
admin.site.register(Transaction)
admin.site.register(Loan)
admin.site.register(Payment)
admin.site.register(BlogPost)