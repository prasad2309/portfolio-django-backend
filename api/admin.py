from django.contrib import admin
from .models import Project, Education

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'imagePath', 'githubLink')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('university', 'major', 'gpa', 'time', 'courses','logoUrl')
