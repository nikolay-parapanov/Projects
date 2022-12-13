from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class MarketItems(models.Model):
    TYPE_MAX_LEN = 4
    NEW = 'new'
    USED = 'used'
    ITEM_TYPE_CHOICES = [
        (NEW, 'new'),
        (USED, 'used'),
    ]
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
        ),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0),
        ),
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=ITEM_TYPE_CHOICES,
        default=NEW,
        )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

