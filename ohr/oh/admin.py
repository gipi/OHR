from django.contrib import admin

from licensing.models import License


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    pass

