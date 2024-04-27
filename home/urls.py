from django.urls import path
from home.views import get_info
from home.views import get_info_1

urlpatterns = [
    path('app_url', get_info, name='app_url'),
    path('app_url_1', get_info_1, name='app_url_1')
]


