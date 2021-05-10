from django.contrib import admin
from . import models

# Register your models here.
class SnapshotInline(admin.TabularInline):
    model = models.Snapshot

class ProjectAdmin(admin.ModelAdmin):
    inlines = [SnapshotInline]

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Tags)
admin.site.register(models.Snapshot)