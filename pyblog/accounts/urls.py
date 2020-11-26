from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.sugnup_views, name='signup'),
    url(r'^login/$', views.login_views, name="login"),
    url(r'^logout/$', views.logout_views, name="logout")
]
