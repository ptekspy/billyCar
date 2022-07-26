import io
from django.contrib import admin
from django.http import FileResponse, HttpResponse
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _
from django_object_actions import DjangoObjectActions
from django.utils.html import format_html
from PIL import Image, ImageDraw, ImageFont

# Register your models here.
from contract.models import Contract

title_font = ImageFont.load_default()


@admin.register(Contract)
class ContractAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ("reference", "building", "customer", "car",
                    "returnDateTime", "returnedAt", "createdAt", "download_link")
    ordering = ("reference", "createdAt", "returnedAt")
    list_filter = ("building", )
    search_fields = ("reference", "building__building_abbr", "customer__name", "customer__cont", "car__license", "car__model")
    readonly_fields = ('download_link', "reference")
    save_as = True

    def get_urls(self):
        urls = super(ContractAdmin, self).get_urls()
        urls += [
            path('download-file/<pk>', self.download_file,
                 name='applabel_modelname_download-file'),
        ]
        return urls

    # custom "field" that returns a link to the custom function
    def download_link(self, obj):
        return format_html(
            '<a href="{}">{}</a>',
            reverse('admin:applabel_modelname_download-file', args=[obj.pk]),
            _("Generate Contract")
        )
    download_link.short_description = _("Generate Contract")

    # add custom view function that downloads the file
    def download_file(self, request, pk):
        # response = HttpResponse(content_type='application/force-download')
        # response['Content-Disposition'] = 'attachment; filename="whatever.png"'
        # generate dynamic file content using object pk
        my_image = Image.open("contract.png")
        image_editable = ImageDraw.Draw(my_image)

        def addText(pos, text):
            image_editable.text(pos, text, (0, 0, 0), font=title_font)
        obj = Contract.objects.get(pk=pk)
        image_editable.text((1350, 110), obj.reference,
                            (0, 0, 0), font=title_font)

        addText((130, 270), f"€{obj.amount_to_pay}" if obj.amount_to_pay  else '   ')
        addText((130, 370), f"{obj.paid_by if obj.paid_by else 'N/A'}")

        addText((120, 485), obj.customer.name)
        addText((120, 535), obj.customer.email)
        addText((120, 595), obj.customer.address.line_one)
        addText((120, 645), obj.customer.address.line_two)
        addText((120, 695), obj.customer.address.line_three)
        addText((120, 750), obj.customer.address.line_four)
        addText((610, 750), obj.customer.cont)
        addText((120, 815), obj.customer.address.property_type)
        # buff = io.BytesIO()
        response = HttpResponse(content_type="image/png")
        my_image.save(response, format='png')
        # response.write(buff)
        return response

        red.save(response, "JPEG")
        return response


# customer = {
#     "name": "John Doe",
#     "email": "email@email.com",
#     "address": {
#         "line_one": "123 Main St",
#         "line_two": "Apt. 456",
#         "line_three": "Anytown, CA 12345",
#         "line_four": "USA",
#         "property_type": "Client"
#     },
#     "cont": "123456789"
# }

# add_customer_info(customer)
