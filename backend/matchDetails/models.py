from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField


class MatchDetails(models.Model):
    matchId = models.BigIntegerField(unique=True, blank=False, null=False)
    response = JSONField()
    created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.matchId)
