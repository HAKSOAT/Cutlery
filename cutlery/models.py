from django.db import models
from django.utils import timezone

# Create your models here.


class URLs(models.Model):
    time_created = models.DateTimeField()
    link = models.URLField(unique=True)
    alias = models.TextField(max_length=32)

    def save(self, *args, **kwargs):
        self.time_created = timezone.now()
        return super(URLs, self).save(*args, **kwargs)

    def __str__(self):
        return "Link: {} \t Alias: {}".format(self.link, self.alias)
