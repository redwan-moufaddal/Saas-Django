from django.db import models

class Notes(models.Model):
    name = models.CharField(max_length=50)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)