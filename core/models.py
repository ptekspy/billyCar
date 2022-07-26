from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    building_name = models.TextField(
        max_length=500, blank=False, null=False, verbose_name=_('building name'))
    building_abbr = models.CharField(
        max_length=2, blank=False, null=False, verbose_name=_('building abbr'))

    class Meta:
        verbose_name = _('building')
        verbose_name_plural = _('buildings')

        def __str__(self) -> str:
            return self.building_name
