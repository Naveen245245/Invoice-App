from django.contrib import admin
from .models import Receiver
from import_export import resources
from import_export.admin import ExportActionMixin


class ReceiverResource(resources.ModelResource):
    class Meta:
        model = Receiver
        fields = ('id', 'name', 'address', 'website', 'created')
        export_order = ('website', 'created', 'address', 'name', 'id')


class ReceiverAdmin(ExportActionMixin, admin.ModelAdmin):
    resources_class = ReceiverResource


admin.site.register(Receiver, ReceiverAdmin)
