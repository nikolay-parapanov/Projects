from django.urls import path, include
from tri.marketplace.views import MarketplaceListView, MarketplaceDetailsView, MarketplaceItemCreateView, \
    MarketplaceItemUpdateView, MarketplaceItemDeleteView

urlpatterns = (
    path('', MarketplaceListView.as_view(), name='marketplace list'),
    path('add/', MarketplaceItemCreateView.as_view(), name='marketplace item add'),
    path('details/<int:pk>/', MarketplaceDetailsView.as_view(), name='marketplace item details'),
    path('edit/<int:pk>/', MarketplaceItemUpdateView.as_view(), name='marketplace item edit'),
    path('delete/<int:pk>/', MarketplaceItemDeleteView.as_view(), name='marketplace item delete'),

    )
