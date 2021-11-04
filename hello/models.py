from django.db import models

class Document(models.Model):
    comment = models.CharField(max_length = 200)
    status = models.CharField(max_length=50)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length= 20)