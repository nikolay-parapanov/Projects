from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from tri.authh.models import AppUser
from tri.marketplace import models as models
from tri.marketplace.forms import MarketplaceItemCreateForm
from tri.marketplace.models import MarketItems


class MarketplaceListView(views.ListView):
    model = models.MarketItems
    template_name = 'marketplace/marketplace-list.html'
    default_paginate_by = 3

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.default_paginate_by)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('id')
        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(name__icontains=pattern.lower())
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class MarketplaceDetailsView(views.DetailView):
    template_name = 'marketplace/marketplace-item-detail.html'
    model = models.MarketItems

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        item = kwargs['object']

        context['is_owner'] = self.request.user.id == item.user_id

        user_from_user_table = AppUser.objects.get(pk=item.user_id)
        context['user_from_user_table'] = user_from_user_table
        context['user_full_name'] = f'{user_from_user_table.first_name} {user_from_user_table.last_name}'
        market_admins = AppUser.objects.filter(is_staff=1, username__icontains="staff_marketplace_")
        superusers = AppUser.objects.filter(is_superuser=1)
        context['has_market_admin_rights'] = False

        context['is_superuser'] = False
        if self.request.user in superusers:
            context['is_superuser'] = True
        else:
            for market_admin in market_admins:
                if market_admin.username == self.request.user.username:
                    context['has_market_admin_rights'] = True

        return context


class MarketplaceItemCreateView(views.CreateView, MarketplaceItemCreateForm):
    template_name = 'marketplace/marketplace-item-add.html'
    model = models.MarketItems
    form_class = MarketplaceItemCreateForm

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        last_object_in_items = MarketItems.objects.last()
        last_object_in_items.user_id = request.user.pk
        last_object_in_items.save()
        return response

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('marketplace item details', kwargs={
            'pk': created_object.pk,
        })


class MarketplaceItemDeleteView(views.DeleteView):
    template_name = 'marketplace/marketplace-item-delete.html'
    model = MarketItems
    success_url = '/'


class MarketplaceItemUpdateView(views.UpdateView):
    template_name = 'marketplace/marketplace-item-edit.html'
    fields = ['name', 'description', 'price', 'type']
    model = MarketItems


    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('marketplace item details', kwargs={
            'pk': created_object.pk,

        })
