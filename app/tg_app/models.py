from django.db import models


class Task(models.Model):
    user_id = models.BigIntegerField(null=False, blank=True)
    message = models.CharField()
    tag = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notice_time_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user_id} — {self.message[:30]}"
