from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    name = models.CharField("Name of User", blank=True, max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField("Bio", blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True)
    country = CountryField("Country", blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("user_detail", kwargs={"username": self.username})
