from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

UserModel = get_user_model()


class UsersListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'profile/profile-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # user_id = int(context['object'].id)
        # profile_data = Profile.objects.filter(pk=user_id).get()
        # context['first_name_for_form'] = profile_data.first_name
        # context['last_name_for_form'] = profile_data.last_name
        # context['age_for_form'] = profile_data.age
        return context


class UserUpdateView(UpdateView):
    fields = '__all__'
    model = UserModel
    template_name = 'profile/profile-edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # user_id = int(context['object'].id)
        # profile_data = Profile.objects.filter(pk=user_id).get()
        # context['first_name_for_form'] = profile_data.first_name
        # context['last_name_for_form'] = profile_data.last_name
        # context['age_for_form'] = profile_data.age
        return context

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('profile details', kwargs={
            'pk': created_object.pk,
        })


class UserDeleteView(DeleteView):
    fields = ('email',)
    model = UserModel
    template_name = 'profile/profile-delete.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def about(request):
    if request.method == "GET":
        return render(request,'web/about.html')
