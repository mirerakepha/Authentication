from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic')      # Columns in list view
    search_fields = ('user__username', 'bio')          # Searchable fields
    list_filter = ('user__is_staff', 'user__is_active')  # Side filters

# Optional: Extend the default User admin to show Profile inline
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(DefaultUserAdmin):
    inlines = (ProfileInline,)

# Unregister and re-register User to attach ProfileInline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
