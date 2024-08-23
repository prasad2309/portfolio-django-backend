from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagePath = models.CharField(max_length=200)
    githubLink = models.URLField()

    def __str__(self):
        return self.title

class Education(models.Model):
    university = models.CharField(max_length=200)
    major = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    time = models.CharField(max_length=200)
    courses = models.CharField(max_length=200)
    logoUrl = models.CharField(max_length=200)

    def __str__(self):
        return self.university
