from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(help_text="Number of Pages")
    publisher = models.CharField(max_length=40)
    pubdate = models.DateField(help_text="Date Published")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
