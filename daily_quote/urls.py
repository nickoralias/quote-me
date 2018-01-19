from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rank_quote/$', views.rank_quote, name='rank_quote'),
    url(r'^(?P<username>.+)/$', views.user_profile, name='profile'),
]
