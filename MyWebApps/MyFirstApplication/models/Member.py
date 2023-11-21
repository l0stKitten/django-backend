from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User
from .GroupChat import GroupChat

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    groupchat_id = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    MEMBER_TYPE = [(0, 'normal'), (1, 'admin')]
    member_type = models.IntegerField(null=False, choices=MEMBER_TYPE, default=0)

class Meta:
    ordering = ['user_id', 'groupchat_id', 'member_type']

def __str__(self):
    return " %d %d %d" % (self.user_id, self.groupchat_id, self.member_type)