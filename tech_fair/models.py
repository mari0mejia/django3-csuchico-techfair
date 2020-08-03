from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length = 250)
    date = models.DateField()

    def __str__(self):
        return self.title

