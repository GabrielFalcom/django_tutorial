from django.shortcuts import render
from django.http import HttpResponse
from django_auth_ldap.backend import LDAPBackend
from accounts.models import UserLdap
# Create your views here.

def home(request):
	args = {'current_user': request.user}
	user = LDAPBackend().authenticate(request, 'gabrielnps','Php3t4@!')
	print(user)
	if user is None:
		raise Exception('No user named found')
	return render(request, 'accounts/home.html',args)

    # numbers = [1,2,3,4,5]
    # name = 'Gabriel'
    # args = {'name': name, 'numbers':numbers}

    # return render(request, 'accounts/login.html',args)

    # return HttpResponse('<em>Home Page!</em>')
