from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

class Location(models.Model):
    userId = models.CharField(max_length=20)
    lat = models.FloatField
    long = models.FloatField
