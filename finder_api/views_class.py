from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from finder_api.forms import RegisterForm

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'app/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app/password/password_reset.html'
    email_template_name = 'app/password/password_reset_email.html'
    subject_template_name = 'app/password/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                        "if an account exists with the email you entered. You should receive them shortly." \
                        " If you don't receive an email, " \
                        "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')
