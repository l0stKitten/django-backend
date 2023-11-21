from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(unique=True, blank=False, null=False, max_length=40)

class Meta:
    ordering = ['category']

def __str__(self):
    return " %s " % (self.category)