from django.db import models

from users.models import ExtendUser


class InformationPiece(models.Model):
    subject = models.CharField(max_length=50)
    information = models.TextField()


class UserStatus(models.Model):
    # de facut formular
    status_mood = models.CharField(max_length=50)  # poate int
    status_energy = models.CharField(max_length=50)  # poate int
    status_sleep_day = models.IntegerField(null=False)




