from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User
import requests
from .forms import CreateUserForm
from django.contrib import messages

# def login(request):
# 	return render(request, 'accounts/login.html')


def profile(request):
	return render(request, 'accounts/profile.html')


class ProfilePage(TemplateView):
	template_name = 'registration/profile.html'

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Учетная запись была создана для ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'registration/register.html', context)


# def login(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.info(request, 'Неверное имя пользователя или пароль')

#         context = {}
#         return render(request, 'registration/login.html', context)


class LoginView(TemplateView):
	template_name = 'registration/login.html'

	def dispatch(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				context['error'] = "Логин или пароль неправильные"
		return render(request, 'registration/login.html', context)


class RegisterView(TemplateView):
	# template_name = 'registration/register.html'
	def dispatch(self, request, *args, **kwargs):
		if request.method == 'POST':
			username = request.POST.get('username')
			email = request.POST.get('email')
			password1 = request.POST.get('password')
			password2 = request.POST.get('password_again')

			if password1 == password2:
				User.objects.create_user(username, email, password)
				return redirect(reverse("login"))
			else:
				print("Пароли не совпадают")

		return render(request, 'registration/register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def passwordReset(request):
	return redirect(request, 'accounts/password_reset_form.html')
