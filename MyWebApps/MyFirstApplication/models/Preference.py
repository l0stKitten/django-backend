from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

class Preference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    preference = models.CharField(unique=False, blank=False, null=False, max_length=40)

class Meta:
    ordering = ['preference']

def __str__(self):
    return f"{self.preference}"