# django imports
from django.db import models
from model_utils.models import TimeStampedModel

# standard imports
import uuid

# custom imports
from .managers import MemeManager

class Meme(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(db_index=True,unique=True, editable=False)

    objects = MemeManager()

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)
