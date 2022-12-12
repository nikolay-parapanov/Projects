from django.urls import path, include
from tri.marketplace.views import MarketplaceListView, MarketplaceDetailsView, MarketplaceItemCreateView

urlpatterns = (
    path('', MarketplaceListView.as_view(), name='marketplace list'),
    path('add/', MarketplaceItemCreateView.as_view(), name='marketplace item add'),
    path('details/<int:pk>/', MarketplaceDetailsView.as_view(), name='marketplace item details'),

    )
