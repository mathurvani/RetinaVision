from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Register custom Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birth_date')
    search_fields = ('user__username', 'bio')

admin.site.register(Profile, ProfileAdmin)

# Extend the default User admin to include related Profile data
class UserAdmin(BaseUserAdmin):
    # Define the fields to be displayed in the User list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

    # Add or customize fields for the User edit view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions')

# Unregister the default User admin and register the customized version
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
