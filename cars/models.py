from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    model = models.CharField(max_length=200, verbose_name=_('model'))
    license = models.CharField(max_length=200, verbose_name=_('license'))
    owner = models.CharField(max_length=200, verbose_name=_('owner'))

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')
        
    def __str__(self) -> str:
        return f"{self.model} - {self.owner}"
