# Create your models here.

from django.db import models


class Book(models.Model):
    UNIVERSITY = 'UN'
    ART = 'AR'
    SCIENCE = 'SC'
    KIDS = 'KD'
    BOOK_FIELD_CHOICES = (
        (UNIVERSITY, 'University'),
        (ART, 'Art'),
        (SCIENCE, 'Science'),
        (KIDS, 'Kids'),
    )

    id_book = models.IntegerField()
    name = models.CharField(max_length=100)
    # image=models.ImageField()
    author = models.CharField(max_length=100)
    edition = models.IntegerField(default=1)
    field = models.CharField(max_length=100, choices=BOOK_FIELD_CHOICES, default=ART)
    price = models.IntegerField(default=0)


    def __unicode__(self):
        return '%s' % self.id_book
