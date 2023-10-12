from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    areas = models.ManyToManyField('Area', related_name='mentors')
    available_hours = models.ManyToManyField('Availability', related_name='mentors', blank=True)

    def __str__(self):
        return f"Mentor {self.email}"

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentors"


class Availability(models.Model):
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    hour = models.DateTimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.mentor.user.username} - {self.hour}"

    class Meta:
        verbose_name = "Availability"
        verbose_name_plural = "Availabilities"


class Area(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"


class Meeting(models.Model):
    start = models.ForeignKey('Availability', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    room = models.ForeignKey('GoogleMeetRoom', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meetings', null=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentored_meetings')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    udated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"Meeting {self.id}"

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"

class GoogleMeetRoom(models.Model):
    room_name = models.CharField(max_length=100)
    room_link = models.URLField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room_name} - {self.room_link}"

    class Meta:
        verbose_name = "GoogleMeetRoom"
        verbose_name_plural = "GoogleMeetRooms"