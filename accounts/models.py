from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     Name = models.CharField(max_length=50)
     Short_Bio = models.TextField(validators = [MinLengthValidator(255, "Bio must be more than 255 characters.")])
