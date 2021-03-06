# Generated by Django 3.2 on 2021-05-03 20:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.CharField(blank=True, max_length=300, validators=[django.core.validators.RegexValidator('^(http:\\/\\/www\\.|https:\\/\\/www\\.|http:\\/\\/|https:\\/\\/)?[a-z0-9]+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$', 'Invalid URL')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo_url',
            field=models.CharField(blank=True, max_length=300, validators=[django.core.validators.RegexValidator('^(http:\\/\\/www\\.|https:\\/\\/www\\.|http:\\/\\/|https:\\/\\/)?[a-z0-9]+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$', 'Invalid URL')]),
        ),
    ]
