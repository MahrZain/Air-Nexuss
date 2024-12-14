from django.db import models





# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    city = models.TextField(null=False, blank=False)
    state = models.TextField(null=False, blank=False)
    

    def __str__(self):
        return self.name