from django.contrib import admin
from .models import Channel
from import_export.admin import ImportExportModelAdmin


class ChannelAdmin(ImportExportModelAdmin):
    list_display = ['channel_name', 'user', 'status']

admin.site.register(Channel, ChannelAdmin)