from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class advisior_info(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    advisior_name = models.CharField(max_length=100)
    advisior_profile_pic = models.URLField()
    def __str__(self):
        return str(self.username)