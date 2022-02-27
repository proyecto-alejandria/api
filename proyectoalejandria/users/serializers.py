from djoser.serializers import UserSerializer

from .models import User


class CurrentUserSerializer(UserSerializer):
    def to_representation(self, instance: User) -> dict:
        data = super().to_representation(instance)
        data["permissions"] = instance.get_all_permissions()
        if instance.is_staff:
            data["permissions"].add("admin.is_staff")
        return data
