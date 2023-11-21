from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User
from .Post import Post
from .Challenge import Challenge

class Participation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    iscompleted = models.BooleanField(null=False, default=False)

class Meta:
    ordering = ['id', 'user_id', 'challenge_id']

def __str__(self):
    return " %d %d %d %s" % (self.id, self.challenge_id, self.post_id, self.iscompleted)