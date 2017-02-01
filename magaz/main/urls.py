from django.conf.urls import *
from blog.views import home, item, index

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls))
    url(r'^$', home),
    url(r'^item/(?P<alias>[^/]+)', item),
]
