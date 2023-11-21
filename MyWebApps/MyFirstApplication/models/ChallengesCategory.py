from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .Challenge import Challenge
from .Category import Category

class ChallengesCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Meta:
    ordering = ['id', 'challenge_id', 'category_id']

def __str__(self):
    return " %d %d %d " % (self.id, self.challenge_id, self.category_id)