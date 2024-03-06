from django.contrib import admin
from .models import User, userProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email','username','role','is_superadmin','is_admin','is_active','last_login')
    ordering =('-date_joined',) #hyphen means descending order
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User,CustomUserAdmin)
admin.site.register(userProfile)