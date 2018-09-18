from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    """docstring for UserProfile."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

def __str__(self):
    return '%s' %(self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
