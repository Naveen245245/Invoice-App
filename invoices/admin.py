from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.dispatch import receiver
from .models import Invoice, Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource

class InvoiceResource(resources.ModelResource):
    profile = Field()
    receiver = Field()
    created = Field()
    closed = Field()
    positions = Field()
    total_amount = Field()

    class Meta:
        model = Invoice
        fields = ("id", "profile", "receiver", "number", "completion_date", "issue_date",
                  "payment_date", "created", "closed", "positions", "total_amount")

    def dehydrate_profile(self, obj):
        return obj.profile.user.username

    def dehydrate_receiver(self, obj):
        return obj.receiver.name

    def dehydrate_created(self, obj):
        return obj.created.strftime("%d-%m-%y")

    def dehydrate_closed(self, obj):
        if obj.closed == True:
            return"True"
        else:
            return "False"

    def dehydrate_positions(self, obj):
        positions_list = [x.title for x in obj.positions]
        position_string = ", ".join(positions_list)
        return position_string

    def dehydrate_total_amount(self, obj):
        return obj.total_amount


class InvoiceAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = InvoiceResource


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Tag, TagAdmin)
