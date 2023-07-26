from django.db import models
from datetime import datetime


# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    createdDate = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title