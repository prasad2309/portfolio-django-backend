from django.urls import path
from .views import ProjectList, EducationList

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('education/', EducationList.as_view(), name='education-list'),
]
