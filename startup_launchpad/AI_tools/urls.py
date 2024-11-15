from django.urls import path
from . import views


urlpatterns = [
    path('ai_tools/',views.aiToolsMainPage,name="ai_tools")
]

