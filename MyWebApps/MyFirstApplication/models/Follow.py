from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

import uuid

User = get_user_model()

class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2user')
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    MEMBER_TYPE = [(0, '->'), (1, '<-'), (2, '<->')]
    follow_type = models.IntegerField(null=False, choices=MEMBER_TYPE, default=0)

    class Meta:
        ordering = ['id', 'user_id', 'seguidor']

    def __str__(self):
        return f"{self.id} {self.user_id} {self.seguidor} {self.follow_type}" 