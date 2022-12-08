from django.urls import path
from tri.web.views import UsersListView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),

)