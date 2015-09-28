from django.db import models
from taggit.managers import TaggableManager
from django.contrib import admin
from config import settings


def resolve_upload_path(prefix):
    def _resolve(instance, filename):
        return '%s/%s/%s' % (instance.name, prefix, filename)

    return _resolve

def resolve_upload_path_image(instance, filename):
    return resolve_upload_path('images')

def resolve_upload_path_schematics(instance, filename):
    return resolve_upload_path('schematics')

def resolve_upload_path_layout(instance, filename):
    return resolve_upload_path('layout')

class OpenHardware(models.Model):
    '''
    This model represents the Open Hardware device linked with all the
    available informations.
    '''

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)

    url        = models.URLField(help_text=u'Main site')
    image      = models.ImageField(upload_to=resolve_upload_path_image) # TODO: multiple images
    schematics = models.FileField(upload_to=resolve_upload_path_schematics)
    layout     = models.FileField(upload_to=resolve_upload_path_layout)

    tags = TaggableManager()

    def __unicode__(self):
        return self.name

class OpenHardwareLike(models.Model):
    '''
    Connect the User to the Open Hardware she likes.
    '''
    user = models.ForeignKey(settings.common.AUTH_USER_MODEL)
    oh   = models.ForeignKey(OpenHardware)

    @staticmethod
    def get_oh_for_user(user):
        return [_.oh for _ in OpenHardwareLike.objects.filter(user=user)]


@admin.register(OpenHardware)
class OpenHardwareAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'short_description',
    ]