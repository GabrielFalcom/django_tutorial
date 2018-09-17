from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserLdap(models.Model):
	User = models.OneToOneField(User,on_delete=models.CASCADE)
	uid = models.CharField(max_length=100)
	displayname = models.CharField(max_length=100)
	departmentnumber = models.CharField(max_length=100)
	cpf = models.CharField(max_length=100)
	empresa = models.CharField(max_length=100)
	mail = models.CharField(max_length=100)
	matricula = models.IntegerField(default='')