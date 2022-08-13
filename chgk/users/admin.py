from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminConfig(UserAdmin):
    search_fields = (
        'username',
        'age',
        'pants_color',
        'relationship_status',
    )
    list_filter = (
        'username',
        'age',
        'pants_color',
        'relationship_status',
        'is_active',
        'is_staff',
    )
    ordering = ('id',)
    list_display = (
        'username',
        'age',
        'pants_color',
        'relationship_status',
        'is_active',
        'is_staff',
    )
    fieldsets = (
        (None, {'fields': (
            'username',
            'age',
            'pants_color',
            'relationship_status',
        )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'age',
                'pants_color',
                'relationship_status',
            )
        }),
    )


admin.site.register(User, UserAdminConfig)
