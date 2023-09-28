from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    areas = models.ManyToManyField('Area', related_name='mentors')

    def __str__(self):
        return f"Mentor {self.email}"


class Area(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meetings(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meetings', null=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentored_meetings')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Meeting {self.id}"