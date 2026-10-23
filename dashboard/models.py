from django.db import models


class ProjectMetric(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    badge_text = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
