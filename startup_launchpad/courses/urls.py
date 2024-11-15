from django.urls import path
from . import views


urlpatterns = [
    path('course-list/',views.courseListPage,name="course-list")
]

