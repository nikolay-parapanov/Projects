from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework import generics as rest_views
from rest_framework import serializers

from tri.authh.models import AppUser
from tri.marketplace.models import MarketItems

UserModel = get_user_model()


class UsersListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['superuser_list'] = AppUser.objects.filter(is_superuser=1)
        context['profile_admins'] = AppUser.objects.filter(is_staff=1, username__icontains="staff_profiles_")
        context['marketplace_admins'] = AppUser.objects.filter(is_staff=1, username__icontains="staff_marketplace_")
        return context


class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'profile/profile-details.html'



    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = kwargs['object'].pk
        context['is_owner'] = self.request.user == self.object
        superusers = AppUser.objects.filter(is_superuser=1)
        profile_admins = AppUser.objects.filter(is_staff=1, username__icontains="staff_profiles_")
        market_admins = AppUser.objects.filter(is_staff=1, username__icontains="staff_marketplace_")
        context['is_superuser'] = False
        context['has_profile_admin_rights'] = False
        context['has_market_admin_rights'] = False

        if self.request.user in superusers:
            context['is_superuser'] = True
        if self.request.user in profile_admins:
            context['has_profile_admin_rights'] = True
        if self.request.user in market_admins:
            context['has_market_admin_rights'] = True

        context['items_listed_by_user'] = MarketItems.objects.filter(user_id=current_user_id)

        return context


class UserUpdateView(UpdateView):
    fields = ['first_name', 'last_name', 'age', 'profile_pic']
    model = UserModel
    template_name = 'profile/profile-edit.html'

    def get(self, request, *args, **kwargs):
        display_user = None
        try:
            display_user = AppUser.objects.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            return redirect("marketplace list")

        superusers = AppUser.objects.filter(is_superuser=1)
        profile_admins = AppUser.objects.filter(is_staff=1, username__icontains="staff_profiles_")
        if self.request.user != display_user and not self.request.user in profile_admins \
                and not self.request.user in superusers:
            raise PermissionDenied("You are not allowed to view this page!")

        request = super().get(self, request, *args, **kwargs)
        return request

    def post(self, request, *args, **kwargs):
        response = super().post(self, request, *args, **kwargs)
        # if self.request.user.pk != kwargs['pk']
        #     response
        return response

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
        return render(request, 'web/about.html')


class ShortProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name', 'email']

class MartketItemsSerializer(serializers.ModelSerializer):
    user = ShortProfileSerializer()
    class Meta:
        model = MarketItems
        fields = '__all__'


class MarketItemsListApiView(rest_views.ListCreateAPIView):
    queryset = MarketItems.objects.all()
    serializer_class = MartketItemsSerializer


class ShortMarketItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItems
        fields = ['name']


class ProfileSerializer(serializers.ModelSerializer):
    market_items = ShortMarketItemsSerializer(many=True)

    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name', 'email', 'market_items']


class ProfilesListApiView(rest_views.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = ProfileSerializer
