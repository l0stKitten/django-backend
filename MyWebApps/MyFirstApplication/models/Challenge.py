from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User

class Challenge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=False, max_length=15)
    description = models.CharField(null=False, blank=False, max_length=700)
    earnedpoints = models.IntegerField(null=False, default=10)
    startDate = models.DateField(auto_now=False, auto_now_add=False, null=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False, null=False)
    createdat = models.DateTimeField(auto_now=True, auto_now_add=False)

class Meta:
    ordering = ['id', 'user_id', 'createdat']

def __str__(self):
    return " %d %d %s" % (self.id, self.user_id, self.title)