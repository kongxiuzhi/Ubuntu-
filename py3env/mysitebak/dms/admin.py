from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','is_staff','is_active']
    ordering = ['created','name']
admin.site.register(User,UserAdmin)
