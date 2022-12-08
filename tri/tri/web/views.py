from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from tri.authh.models import Profile

UserModel = get_user_model()


class UsersListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.user.__class__)
        return context


class UserDetailsView(DetailView):
    template_name = 'profile/profile-details.html'
    model = UserModel
    first_name = Profile.first_name
    last_name = Profile.last_name

    @property
    def full_name(self):