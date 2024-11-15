from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('', include('video_call.urls')),
    path('', include('AI_tools.urls')),
    path('', include('courses.urls')),
    path('', include('Admin.urls')),
]
