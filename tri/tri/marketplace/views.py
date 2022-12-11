from django.urls import reverse_lazy
from django.views import generic as views
from tri.marketplace import models as models


class MarketplaceListView(views.ListView):
    model = models.MarketItems
    template_name = 'marketplace/marketplace-list.html'

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
    template_name = 'marketplace/marketplace-detail-pk.html'
    model = models.MarketItems


class MarketplaceItemCreateView(views.CreateView):
    template_name = 'marketplace/marketplace-item-create.html'
    model = models.MarketItems
    fields = '__all__'
    success_url = 'marketplace/marketplace-list/'

    # def get_success_url(self):
    #     created_object = self.object
    #     return reverse_lazy('marketplace details item', kwargs={
    #         pk:created_object.id
    #     })
