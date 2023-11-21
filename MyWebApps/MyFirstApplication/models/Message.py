from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User
from .GroupChat import GroupChat

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(null=False, blank=False, max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    groupchat_id = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now=True, auto_now_add=False)

class Meta:
    ordering = ['id', 'user_id', 'groupchat_id', 'createdat']

def __str__(self):
    return " %d %d %d %s" % (self.id, self.user_id, self.groupchat_id, self.createdat)