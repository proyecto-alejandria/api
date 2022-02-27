from uuid import (
    UUID,
    uuid4,
)

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    id: "models.UUIDField[UUID, UUID]" = models.UUIDField(
        "identificador",
        primary_key=True,
        editable=False,
        default=uuid4,
    )
