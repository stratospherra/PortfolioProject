from django.db import models
from ..Users.models import User
from ..Users.models import Profile


class Portfolio(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    about_me = models.TextField()
    portfolio_image = models.ImageField(upload_to='portfolios/')

    def __str__(self):
        return self.profile.user.first_name + ' ' + self.profile.user.last_name
# Create your models here.
