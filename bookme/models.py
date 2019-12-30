from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return "Book Title: {}".format(self.title)
