from django.urls import path, include
from tri.marketplace.views import MarketplaceListView, MarketplaceDetailsView, MarketplaceItemCreateView

urlpatterns = (
    path('', MarketplaceListView.as_view(), name='marketplace list'),
    path('new-item/', MarketplaceItemCreateView.as_view(), name='marketplace new item'),
    path('details/<int:pk>/', MarketplaceDetailsView.as_view(), name='marketplace details item'),
        # path('/', MarketDisplayListView.as_view(), name='market display list'),
    )
