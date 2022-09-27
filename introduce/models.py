from django.db import models

# Create your models here.
class Accesslog(models.Model):
    class Meta:
        db_table = "Access_log"
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)