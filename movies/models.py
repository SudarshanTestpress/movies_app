from django.db import models


from phonenumber_field.modelfields import PhoneNumberField


class Studio(models.Model):
    title = models.CharField(max_length=40, unique=True)
    website = models.URLField(max_length=400)
    slug = models.SlugField(max_length=200)


class Genre(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=200)


class Director(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    phone_number = PhoneNumberField(unique=True, blank=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField(max_length=400)
    gender = gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
