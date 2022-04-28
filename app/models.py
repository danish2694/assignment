from tabnanny import verbose
from django.db import models

class Cards(models.Model):
    title           = models.CharField(max_length=255)
    text            = models.CharField(max_length=255)
    date_created    = models.DateTimeField(auto_now_add=True)
    ip_address      = models.CharField(max_length=255)
    time_stamp      = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Cards'
    def __str__(self):
        return self.title
