from django.db import models
from taggit.managers import TaggableManager
from django.contrib import admin



class OpenHardware(models.Model):
    '''
    This model represents the Open Hardware device linked with all the
    available informations.
    '''

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)
    description = models.TextField()

    tags = TaggableManager()

    def __unicode__(self):
        return self.name

@admin.register(OpenHardware)
class OpenHardwareAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'short_description',
    ]