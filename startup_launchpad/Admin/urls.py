from django.urls import path
from . import views


urlpatterns = [
    path('course-list-admin/',views.CourseListAdmin,name="course-list-admin"),
    path('view-students/', views.view_students, name="view-students"),
    path('view-startup/', views.view_startup, name="view-startup")
]