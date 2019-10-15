from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^$', index, name='index')
    url(r'^display_laptop$', display_laptop, name='display_laptop')
]