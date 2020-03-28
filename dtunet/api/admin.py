from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','label','bio','image','is_online','following')}),
        ('Other details', {'fields': ('is_admin','is_active')}),
    )
    list_display = ('email', 'name','label')
    list_filter = ('label',)
    search_fields = ('email',)
    ordering = ('email',)
    add_fieldsets = (
        (None, {
            #'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)
