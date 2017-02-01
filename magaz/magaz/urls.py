from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import home, item
import main.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'magaz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),
    url(r'^item/(?P<alias>[^/]+)', 'main.views.item'),
    #url(r'^(?P<alias>[^/]+)', 'main.views.get_category'),
]
