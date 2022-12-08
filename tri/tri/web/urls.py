from django.urls import path, include
from tri.web.views import UsersListView, UserDetailsView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
    path('profile/<int:pk>', include([
        path('', UserDetailsView.as_view(), name='profile details' )
    ]))

)