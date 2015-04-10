from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.contrib import messages
from .models import Profile
from .forms import EditProfileForm, RegisterForm, LoginForm

from django.utils.text import slugify


    

class ProfileView(UpdateView):
    model = Profile
    template_name = 'profile.html'
    form_class = EditProfileForm




def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


'''
test these two functionally
'''


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        slug = slugify(self.request.POST['username'])

        user = authenticate(username=username, password=password)
        profile = Profile.objects.create(
            user=user,slug=slug
        )
        login(self.request, user)
        
        self.success_url = reverse('profiles:profile', args=[slug])
        return super(RegisterView, self).form_valid(form)




class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        self.success_url = reverse('profiles:profile', args=[username])
        return super(LoginView, self).form_valid(form)