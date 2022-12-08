from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


UserModel = get_user_model()

class UsersListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # context['has_email'] = AppUser.has_email(self.request.user)
        print(self.request.user.__class__)

        return context
