from django.conf.urls import include, url
from django.contrib import admin
from core.views import FormView

urlpatterns = [
    # Examples:
    # url(r'^$', 'projeto2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FormView.as_view()),
    url(r'^(?P<id_empresa>\w+)/(?P<id_torre>\w+)$', FormView.as_view(), name='form_view'),
]
