# Generated by Django 3.2.6 on 2021-09-16 11:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=40)),
                ("middle_name", models.CharField(blank=True, max_length=40)),
                ("last_name", models.CharField(max_length=40)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None, unique=True
                    ),
                ),
                ("birthdate", models.DateField()),
                ("website", models.URLField(max_length=400)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=40, unique=True)),
                ("slug", models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Studio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=40, unique=True)),
                ("website", models.URLField(max_length=400)),
                ("slug", models.SlugField(max_length=200)),
            ],
        ),
    ]
