from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "profile",
        "first_name",
        "last_name",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Informações Pessoais",
            {"fields": ("first_name", "last_name", "email", "profile")},
        ),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, UserAdmin)
