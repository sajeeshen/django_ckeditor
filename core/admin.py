from django.contrib import admin
from core.models import Jobs


# Register your models here.

class JobsAdmin(admin.ModelAdmin):
    list_display = ("title", "job_type", "created")


admin.site.register(Jobs, JobsAdmin)
