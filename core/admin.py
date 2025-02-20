from django.contrib import admin
from core.models import Video
from import_export.admin import ImportExportModelAdmin


class VideoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
