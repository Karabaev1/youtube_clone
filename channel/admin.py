from django.contrib import admin
from channel.models import Channel
from import_export.admin import ImportExportModelAdmin


class VideoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Channel)