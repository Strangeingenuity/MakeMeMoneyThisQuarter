from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    #/music/71(this number is an id of the stockcode
    url(r'^(?P<StockCode_id>[0-9]+)/$', views.detail, name='detail'),


]
