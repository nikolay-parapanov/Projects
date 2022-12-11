from django.urls import path, include

from tri.web.views import UsersListView, about, UserDetailsView, UserUpdateView, UserDeleteView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile details' ),
        path('edit/', UserUpdateView.as_view(), name='profile update' ),
        path('delete/', UserDeleteView.as_view(), name='profile delete' ),
    ]))
)