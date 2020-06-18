from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(blank=True,null=True)
    imafe= models.FileField(upload_to='images/',blank=True,null=True)
    