from django.views import generic as views

from tri.marketplace.models import MarketItems


class MarketplaceListView(views.ListView):
    model = MarketItems
    template_name = 'marketplace/marketplace-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
