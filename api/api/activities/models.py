from django.db import models

class Activities(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    activity_date = models.DateField()