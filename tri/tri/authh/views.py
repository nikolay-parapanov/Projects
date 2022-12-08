from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tri.authh.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'authh/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    #Automatically sign-in the user after successfull registration
    def form_valid(self, form):
        result= super().form_valid(form)
        login(self.request,self.object)
        return result


class SignInView(LoginView):
    template_name = 'authh/sign-in.html'



class SignOutView(LogoutView):
    next_page = reverse_lazy('index')
