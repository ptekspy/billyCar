from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Address(models.Model):
    line_one = models.CharField(
        max_length=200, verbose_name=_('address line one'))
    line_two = models.CharField(
        max_length=200, verbose_name=_('address line two'))
    line_three = models.CharField(
        max_length=200, verbose_name=_('address line three'))
    line_four = models.CharField(
        max_length=200, verbose_name=_('address line four'))

    CLIENT = 'Client'
    HOME = 'Home'
    BUSINESS = 'Business'
    PROPERTY_TYPE_CHOICES = [
        (CLIENT, _("Client")),
        (HOME, _("Home")),
        (BUSINESS, _("Business")),
    ]
    property_type = models.CharField(
        max_length=8,
        choices=PROPERTY_TYPE_CHOICES,
        default=CLIENT,
        verbose_name=_('property type')
    )

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self) -> str:
        return self.line_one


class DrivingLicense(models.Model):
    number = models.CharField(
        max_length=200, verbose_name=_('driving license number'))
    country = models.CharField(max_length=200, verbose_name=_('country'))
    issued_date = models.DateField(verbose_name=_('issued date'))

    class Meta:
        verbose_name = _('driving license')
        verbose_name_plural = _('driving licenses')

    def __str__(self) -> str:
        return self.number


class Passport(models.Model):
    number = models.CharField(
        max_length=200, verbose_name=_('passport number'))
    country = models.CharField(max_length=200, verbose_name=_('country'))
    expiry_date = models.DateField(verbose_name=_('expiry date'))

    class Meta:
        verbose_name = _('passport')
        verbose_name_plural = _('passports')

    def __str__(self) -> str:
        return self.number


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    email = models.EmailField(max_length=200, verbose_name=_('email'))
    phone = models.CharField(max_length=200, verbose_name=_('phone'))
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    driving_license = models.OneToOneField(
        DrivingLicense, on_delete=models.CASCADE)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE)
    blocked = models.BooleanField(default=False, verbose_name=_('blocked'))
    cont = models.CharField(max_length=50, verbose_name=_('cont no'))

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __str__(self) -> str:
        return self.name

    def contract_count(self) -> int:
        return self.contracts.all().count()
