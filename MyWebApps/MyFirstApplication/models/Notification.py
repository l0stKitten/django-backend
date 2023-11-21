from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .Post import Post

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(null=True, blank=True, max_length=700)
    notification_type = models.CharField(null=False, max_length=15)
    createdat = models.DateTimeField(auto_now=True, auto_now_add=False)
    isread = models.BooleanField(default=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Meta:
    ordering = ['id', 'content', 'createdat']

def __str__(self):
    return " %d %s %s" % (self.id, self.notification_type, self.createdat)