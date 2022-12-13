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
        context['is_owner'] = self.request.user == self.object
        return context

class UserUpdateView(UpdateView):

    fields = ['first_name', 'last_name', 'age']
    model = UserModel
    template_name = 'profile/profile-edit.html'



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
