from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser #, CustomUserManager
from .forms import CustomUserAdminChangeForm, CustomUserAdminCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin): 
    # The forms to add and change user instances
    form = CustomUserAdminChangeForm
    add_form = CustomUserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser,CustomUserAdmin)
# admin.site.register(CustomUserAdmin)

# admin.site.register(CustomUser)
