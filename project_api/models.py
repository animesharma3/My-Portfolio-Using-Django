from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from djrichtextfield.models import RichTextField


url_regex = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
url_validator = RegexValidator(url_regex, "Invalid URL")

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=300)
    finished = models.BooleanField(default=False, blank=True, null=True)
    description = RichTextField()
    demo_url = models.CharField(max_length=300, validators=[url_validator], blank=True)
    github_url = models.CharField(max_length=300, validators=[url_validator], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='projects')
    header_image = models.ImageField(null=True, blank=True, upload_to='images/projects/header')

    def __str__(self):
        return self.title

class Snapshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='snapshots')
    snapshot = models.ImageField(null=True, blank=True, upload_to='images/projects/snapshots')
    created_at = models.DateTimeField(auto_now_add=True)