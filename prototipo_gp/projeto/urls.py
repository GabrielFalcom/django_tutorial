from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.home),
    path('login/',LoginView.as_view(template_name='projeto/login.html'),name="login"),
    path('perfil',views.edit_profile,name='perfil')

]