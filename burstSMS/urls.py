from django.conf.urls import patterns, include, url
from test_app.views import AppIndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'burstSMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', AppIndexView.as_view(), name='home'),
)
