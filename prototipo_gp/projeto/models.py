from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_auth_ldap.backend import LDAPBackend
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usuario = models.CharField(max_length=20, default='')
    matricula = models.IntegerField(default=0)
    cr = models.CharField(max_length=10, default='')
    nome = models.CharField(max_length=60, default='')
    cpf = models.CharField(max_length=15, default='')
    empresa = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=75, default='')

    def __str__(self):
        return '%s' % (self.user)

def create_profile(sender, instance, **kwargs):
    try:
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=instance)
            user = LDAPBackend().populate_user(instance.username)
            if user:
                try:
                    empresa = user.ldap_user.attrs['empresa'][0]
                except:
                    empresa = ''
                matricula = 0
                uid = user.ldap_user.attrs['uid'][0]
                displayname = user.ldap_user.attrs['displayname'][0]
                departmentnumber = user.ldap_user.attrs['departmentnumber'][0]
                cpf = user.ldap_user.attrs['cpf'][0]
                mail = user.ldap_user.attrs['mail'][0]

                user_profile.usuario = uid
                user_profile.matricula = matricula
                user_profile.nome = displayname
                user_profile.cr = departmentnumber
                user_profile.cpf = cpf
                user_profile.empresa = empresa
                user_profile.email = mail
                user_profile.save()
    except Exception as e:
        print('Erro Projeto[Model]=create_profile: ' +str(e))

post_save.connect(create_profile, sender=User)