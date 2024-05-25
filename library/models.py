from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="docs_library")
    add_date = models.DateTimeField(auto_now_add=True)
