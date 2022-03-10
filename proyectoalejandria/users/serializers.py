from djoser.serializers import (
    UserCreateSerializer,
    UserSerializer,
)

from .models import User


USER_FIELDS = ("id", "email", "first_name", "last_name")


class CurrentUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = USER_FIELDS
        read_only_fields = ("id", "email")

    def to_representation(self, instance: User) -> dict:
        data = super().to_representation(instance)
        data["permissions"] = instance.get_all_permissions()
        if instance.is_staff:
            data["permissions"].add("admin.is_staff")
        return data


class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = USER_FIELDS + ("password",)

    def create(self, validated_data: dict) -> User:
        validated_data["username"] = validated_data["email"]
        return super().create(validated_data)
