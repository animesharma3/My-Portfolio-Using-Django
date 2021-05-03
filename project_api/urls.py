from django.urls import path
from . import views

urlpatterns = [
    path('project-list/', views.project_list, name='project-list'),
    path('project-detail/<int:pk>', views.project_detail, name='project-detail'),
]
