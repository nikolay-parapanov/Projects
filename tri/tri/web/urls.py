from django.urls import path, include

from tri.web.views import UsersListView, about, UserDetailsView, UserUpdateView, UserDeleteView, MarketItemsListApiView, \
    ProfilesListApiView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile details'),
        path('edit/', UserUpdateView.as_view(), name='profile update'),
        path('delete/', UserDeleteView.as_view(), name='profile delete'),
    ])),

    path('api/market-items/', MarketItemsListApiView.as_view(), name='api list marketitems'),
    path('api/profiles/', ProfilesListApiView.as_view(), name='api list profiles'),
)
