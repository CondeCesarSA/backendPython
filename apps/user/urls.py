from django.urls import path
from apps.user.views import HomePageView, CreateUserView, UpdateUserView, DeleteUserView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('new/', CreateUserView.as_view(), name='new'),
    path('edit/<int:pk>', UpdateUserView.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteUserView.as_view(), name='delete')

]
