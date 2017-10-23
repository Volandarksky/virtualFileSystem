# -- coding: utf-8 --

from django.db import models

# Create your models here.
class Folder(models.Model):
    path = models.CharField(max_length=80)
    name = models.CharField(max_length=30)
    # root = models.CharField(max_length=30)

    def __unicode__(self):
        return u"Name: %s, Path: %s" % (self.name, self.path)

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"

class File(models.Model):
    path = models.CharField(max_length=80)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u"Name: %s, Path: %s" % (self.name, self.path)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
