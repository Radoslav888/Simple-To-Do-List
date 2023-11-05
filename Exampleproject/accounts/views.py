from django.contrib.auth import views as auth_views, get_user_model, login
from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy

from Exampleproject.accounts.forms import UserCreateForm

# Create your views here.

UserModel = get_user_model()


class SingInView(auth_views.LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy('index')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
