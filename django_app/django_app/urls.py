from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import  *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test', test.as_view(),name='test'),
    url(r'^get', get.as_view(),name='data'),
    url(r'^post', post.as_view(),name='post'),
    url(r'^sam', sample.as_view(),name='data'),
)
