from django.db import models
from ckeditor.fields import RichTextField

JOB_TYPE = (
    ('FULL_TIME', 'FULL TIME'),
    ('PART_TIME', 'PART TIME')
)


class Jobs(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE, default='FULL_TIME', max_length=100)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
