from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView
from project_api.models import Project


# Create your views here.
def index(request):
    myself = User.objects.get(id=1).myself
    return render(request, 'index.html', context={'myself': myself})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-details.html'
     
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data()
        project = Project.objects.get(id=self.kwargs['pk'])
        context['snapshots'] = project.snapshots.values_list()
        return context