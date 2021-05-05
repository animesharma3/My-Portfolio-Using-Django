from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

url_regex = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
url_validator = RegexValidator(url_regex, "Invalid URL")

# Create your models here.
class Myself(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = models.TextField()
    address = models.TextField(default='62, Karamchari Colony, Station Road, Dewas')
    profile_header = models.TextField(default='Data Scientist | Machine Learning Engineer | Full Stack Web Developer')
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    phone_no = models.CharField(max_length=20, default="(+91) 738 966 6837")
    github_profile = models.CharField(max_length=300, validators=[url_validator], blank=True, default='https://www.github.com/animesharma3')
    linkedin_url = models.CharField(max_length=300, validators=[url_validator], blank=True, default='https://www.linkedin.com/in/animesh-sharma-73300a161/')
    kaggle_url = models.CharField(max_length=300, validators=[url_validator], blank=True, default='https://www.kaggle.com/animesharma3')
    twitter_url = models.CharField(max_length=300, validators=[url_validator], blank=True, default='https://www.twitter.com/animesharma3')
    instagram_url = models.CharField(max_length=300, validators=[url_validator], blank=True, default='https://www.instagram.com/animesharma3')
    years_of_experience = models.IntegerField(default=2)
