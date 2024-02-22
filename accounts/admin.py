from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.forms import UserChangeForm, UserCreationForm

# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "email", "is_admin", "is_superuser"]
    list_filter = ["is_superuser", "is_admin"]

    fieldsets = [
        ("Personal Information", {"fields": ["username", "email"]}),
        ("Permissions", {"fields": ["is_admin"]}),
        ("Credentials", {"fields": ["password"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "class": ["wide"],
                "fields": (
                    "username",
                    "email",
                    "password",
                    "confirm_password",
                ),
            },
        )
    ]


from accounts.models import User

admin.site.register(User, UserAdmin)
