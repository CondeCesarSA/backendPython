from django.urls import path
from apps.user.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
