from django.urls import path, include
from tri.authh.views import SignUpView, SignInView, SignOutView
from tri.marketplace.views import MarketplaceListView

urlpatterns = (
    path('marketplace/', include([
        path('list/', MarketplaceListView.as_view(), name='marketplace list')
        # path('/', MarketDisplayListView.as_view(), name='market display list'),
    ])
         ),
)
