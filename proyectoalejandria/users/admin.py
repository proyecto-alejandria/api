from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from rest_framework_simplejwt.token_blacklist.admin import (
    OutstandingTokenAdmin as OriginalOutstandingTokenAdmin,
)
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .models import User


class OutstandingTokenAdmin(OriginalOutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs) -> bool:
        # This allows us to remove users
        # See: https://github.com/jazzband/djangorestframework-simplejwt/issues/266
        return True


admin.site.register(User, UserAdmin)

admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, OutstandingTokenAdmin)
