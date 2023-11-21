from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User
from .Preference import Preference

class UsersPreference(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    preference_id = models.ForeignKey(Preference, on_delete=models.CASCADE)

class Meta:
    ordering = ['user_id', 'preference_id']

def __str__(self):
    return f"{self.user_id} {self.preference_id}"