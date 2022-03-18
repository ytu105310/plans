from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    title = models.TextField(max_length=100, blank=False, default='')

    class Meta:
        ordering = ['date']
