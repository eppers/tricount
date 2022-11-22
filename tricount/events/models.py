from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Event(models.Model):
    label = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)
    settle = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_user", null=False)

    def get_absolute_url(self):
        return reverse("events:event_update", kwargs={"pk": self.pk})
