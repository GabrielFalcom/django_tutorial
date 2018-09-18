from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
# Create your views here.

@login_required
def home(request):
    args = {'current_user': request.user}

    return render(request, 'accounts/home.html',args)

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)
