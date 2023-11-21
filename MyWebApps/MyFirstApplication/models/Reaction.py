from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User
from .Post import Post

class Reaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.CharField(null=False, blank=False, max_length=15)

    class Meta:
        ordering = ['id', 'user_id', 'reaction']

    def __str__(self):
        return " %d %d %s" % (self.id, self.user_id, self.reaction)