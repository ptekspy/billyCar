from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
# Register your models here.
from core.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("building_name", "building_abbr", "view_contracts_link")
    ordering = ("building_name",)
    search_fields = ("building_name", "building_abbr")

    def view_contracts_link(self, obj):
        count = obj.contracts.count()
        url = (
            reverse("admin:contract_contract_changelist")
            + "?"
            + urlencode({"user__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} {}</a>', url, count, _("Contracts"))

    view_contracts_link.short_description = _("Contracts")
