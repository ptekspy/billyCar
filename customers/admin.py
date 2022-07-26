from customers.models import Address, Customer, DrivingLicense, Passport
from contract.models import Contract
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
# Register your models here.


def block_customers(modeladmin, request, queryset):
    queryset.update(blocked=True)


def un_block_customers(modeladmin, request, queryset):
    queryset.update(blocked=False)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "cont", "email", "view_contracts_link", "blocked")
    ordering = ("name", "blocked")
    list_filter = ("blocked", )
    search_fields = ("name", "cont", "email")
    actions = [block_customers, un_block_customers]
    save_as = True

    def view_contracts_link(self, obj):
        count = obj.contracts.count()
        url = (
            reverse("admin:contract_contract_changelist")
            + "?"
            + urlencode({"customer__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} {}</a>', url, count, _("Contracts"))

    view_contracts_link.short_description = _("Contracts")

    def save_model(self, request, obj, form, change):
        # Django always sends this when "Save as new is clicked"
        if '_saveasnew' in request.POST:
            # Get the ID from the admin URL
            original_pk = request.resolver_match.kwargs['object_id']
            print(original_pk)

            # Get the original object
            original_obj = obj._meta.concrete_model.objects.get(id=original_pk)

            # Iterate through all it's properties
            for prop, value in vars(original_obj).items():
                print(prop)
                # setattr(obj, prop, getattr(original_obj, prop))  # Copy it!
        obj.save()


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(DrivingLicense)
class DrivingLicenseAdmin(admin.ModelAdmin):
    list_display = ("number", "country", "issued_date")
    list_filter = ("country", )
    ordering = ("number", "issued_date")
    search_fields = ("number", "country")


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ("number", "country", "expiry_date")
    list_filter = ("country", )
    ordering = ("number", "expiry_date")
    search_fields = ("number", "country")
