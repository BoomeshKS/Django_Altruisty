from django.urls import path
from . import views


urlpatterns = [
    path('overview/',views.overview,name="overview"),
    path('save-swot-analysis/', views.save_swot_analysis, name='save_swot_analysis'),
    path('improvement/',views.improvement,name="improvement"),
    path('create-swot/',views.createswot,name='create-swot'),
    path('strength/',views.strength,name="strength"),
    path('list/',views.list,name="list"),
    path('points/<str:data>',views.points,name="points"),
    path('swot/',views.swot,name="swot"),
    path('',views.index,name="index"),
    path('swotStartNow/', views.swotStartNow, name="swot-start-now"),  # Correct URL
    path('delete-report/<int:report_id>/', views.delete_report, name="delete-report"),
     path('report-detail/<int:id>/', views.report_detail, name='report-detail'),
     path('view-improvement/<int:id>/', views.viewImprovement, name='view-improvement'),
     path('save-improvements/', views.save_improvements, name='save_improvements')
]

