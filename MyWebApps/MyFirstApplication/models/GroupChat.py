from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

class GroupChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=False, blank=False, null=False, max_length=40)
    createdat = models.DateTimeField(auto_now=True, auto_now_add=False)

class Meta:
    ordering = ['name', 'createdat']

def __str__(self):
    return " %s " % (self.name)