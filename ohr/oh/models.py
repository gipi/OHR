from django.contrib import admin
from django.db import models
from taggit.managers import TaggableManager
#from django.utils.text import slugify

from django.conf import settings
from model_utils import Choices
from licensing.models import Licensed


def upload_to_resolver_for_image(instance, filename):
    return '%(name)s/images/%(filename)s' % {
        'name': instance.slug,
        'filename': filename,
    }

def upload_to_resolver(instance, filename):
    return '%(name)s/%(type)s/%(filename)s' % {
        'name': instance.slug,
        'type': instance.type,
        'filename': filename,
    }

class OpenHardware(models.Model):
    '''
    This model represents the Open Hardware device linked with all the
    available informations.
    '''

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)

    url        = models.URLField(help_text=u'Main site')
    image      = models.ImageField(upload_to=upload_to_resolver_for_image) # TODO: multiple images
    slug       = models.SlugField(unique=True)

    tags = TaggableManager()

    def __unicode__(self):
        return self.name

# TODO: use code like <https://github.com/nathan-osman/django-archive/blob/master/django_archive/management/commands/archive.py#L89>
#       to create an archive of all attachments
class OpenHardwareAttachment(Licensed):
    '''
    Link some external document to the OpenHardware instance.
    '''
    TYPES = Choices(
        ('schematics', ('schematics'),),
        ('layout', ('layout'),),
    )
    oh   = models.ForeignKey(OpenHardware)
    type = models.CharField(choices=TYPES, max_length=100)
    file = models.FileField(upload_to=upload_to_resolver)
    description = models.CharField(max_length=100, help_text=u'Indicate for example what program can edit it')

    @property
    def slug(self):
        '''Use the same slug as the OH instance is attached to'''
        return self.oh.slug

class OpenHardwareLike(models.Model):
    '''
    Connect the User to the Open Hardware she likes.
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    oh   = models.ForeignKey(OpenHardware)

    @staticmethod
    def get_oh_for_user(user):
        return [_.oh for _ in OpenHardwareLike.objects.filter(user=user if user.is_authenticated() else None)]



class OpenHardwareAttachmentAdmin(admin.TabularInline):
    model = OpenHardwareAttachment

@admin.register(OpenHardware)
class OpenHardwareAdmin(admin.ModelAdmin):
    inlines = [
        OpenHardwareAttachmentAdmin
    ]
    list_display = [
        'name',
        'short_description',
    ]
    prepopulated_fields = {'slug': ('name',)}

    # FIXME: on save move media files if slug is changed
