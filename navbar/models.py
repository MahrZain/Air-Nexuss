from django.db import models



class Header(models.Model):
    name = models.CharField(blank=False, max_length=100,null=True)
    url = models.URLField(blank=False)
    create = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name


