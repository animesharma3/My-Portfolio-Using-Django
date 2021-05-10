from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='projects'),
]
