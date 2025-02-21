from django.contrib import admin
from .models import User
# Register your models here.
# @admin.register(User)
# class User(admin.ModelAdmin):
#     pass
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # pass  
    model = User
    list_display = ("username", "bio", "role", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("bio", "role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("bio", "role")}),
    )