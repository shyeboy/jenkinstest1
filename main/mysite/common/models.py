from django.db import models


from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=20)

# Create your models here.
