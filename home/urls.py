from django.urls import path
from home.views import get_info

urlpatterns = [
    path('app_url', get_info, name='app_url')
]


