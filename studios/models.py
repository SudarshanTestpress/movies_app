from django.db import models
from django.db.models.deletion import CASCADE
from taggit.managers import TaggableManager
from django.utils.text import slugify


from phonenumber_field.modelfields import PhoneNumberField


class Studio(models.Model):
    title = models.CharField(max_length=40, unique=True)
    website = models.URLField(max_length=400)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Director(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    phone_number = PhoneNumberField(unique=True, blank=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField(max_length=400)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def save(self, *args, **kwargs):
        value = self.first_name + self.last_name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + self.last_name


class Movies(models.Model):
    title = models.CharField(max_length=40, unique=True)
    subtitle = models.URLField(max_length=400)
    slug = models.SlugField(max_length=200)
    directors = models.ManyToManyField(Director)
    studio = models.ForeignKey(Studio, on_delete=CASCADE)
    released_date = models.DateField(auto_now=False, auto_now_add=False)
    cover_image = models.ImageField(upload_to="images", null=True, blank=True)
    review = models.TextField(max_length=1000)
    genre = TaggableManager(blank=True)
    asin = models.IntegerField(unique=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
