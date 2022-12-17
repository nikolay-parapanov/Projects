from django.contrib.auth import login, get_user_model
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from tri.authh.forms import SignUpForm

UserModel=get_user_model()


class SignUpView(views.CreateView):
    template_name = 'authh/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    # fields = ('username', 'password1', 'password2', 'email', 'age', 'profile_pic')

    def post(self, request, *args, **kwargs):
        response = super().post(self, request, *args, **kwargs)

        return response

    #Automatically sign-in the user after successfull registration
    def form_valid(self, form):
        result= super().form_valid(form)
        login(self.request,self.object)
        return result

    # def post(self, request, *args, **kwargs):
    #     response = super().post(self, request, args, kwargs)
    #     return response



class SignInView(auth_views.LoginView):
    template_name = 'authh/sign-in.html'



class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
