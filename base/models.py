from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model

class Team(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  designation = models.CharField(max_length=255)
  photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
  facebook_link = models.URLField(max_length=100)
  twitter_link = models.URLField(max_length=100)
  google_plus_link = models.URLField(max_length=100)
  create_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return (f'{self.first_name} {self.last_name} - {self.designation}')