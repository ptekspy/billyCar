from cars.models import Car
from customers.models import Customer
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contract(models.Model):
    building = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='contracts')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contracts')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='contracts')
    returnDateTime = models.DateTimeField(
        blank=True, null=True, verbose_name=_('return date and time'))
    returnedAt = models.DateTimeField(
        blank=True, null=True, verbose_name=_('returned at'))
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created at'))
    amount_to_pay = models.IntegerField(
        default=0, verbose_name=_('amount to pay'))
    paid_by = models.CharField(max_length=255, verbose_name=_('paid by'), blank=True, null=True)
    
    reference = models.CharField(max_length=255, verbose_name=_('contract reference'), blank=True, null=True)
    

    class Meta:
        verbose_name = _('contract')
        verbose_name_plural = _('contracts')

    def save(self, *args, **kwargs):
        self.reference = f"{self.building.building_abbr}{self.pk}"
        super(Contract, self).save(*args, **kwargs)

    def __str__(self) -> str:
            return f"{self.customer.name} - {self.car.model}"
