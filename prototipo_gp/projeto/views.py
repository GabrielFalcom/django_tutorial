from django.shortcuts import render, redirect
from projeto.forms import EditProfileForm
# Create your views here.

def home(request):
    args = {'current_user': request.user}
    return render(request,'projeto/home.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user.userprofile)
        print(request.user)
        print(request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('/projeto/')
    else:
        form = EditProfileForm(instance=request.user.userprofile)

    args = {'form': form,'current_user': request.user}
    return render(request, 'projeto/perfil.html/',args)
