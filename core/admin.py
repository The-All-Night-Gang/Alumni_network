from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(Group)
admin.site.register(User,ImportExportModelAdmin)
admin.site.register(event)