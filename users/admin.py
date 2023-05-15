from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['surname', 'name', 'middlename', 'phone', 'email']
    list_display_links = ['surname', 'name', 'middlename', 'phone', 'email']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'phone',
                    'status'
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'status'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)