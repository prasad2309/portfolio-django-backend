# Generated by Django 5.1 on 2024-08-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("university", models.CharField(max_length=200)),
                ("major", models.CharField(max_length=100)),
                ("gpa", models.CharField(max_length=100)),
                ("time", models.CharField(max_length=200)),
                ("courses", models.CharField(max_length=200)),
                ("logoUrl", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("imagePath", models.CharField(max_length=200)),
                ("githubLink", models.URLField()),
            ],
        ),
    ]
