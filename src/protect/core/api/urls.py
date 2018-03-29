from django.conf.urls import url

from protect.core.api.views import ApiPersons

help_patterns = [
    url(r'^persons/$', ApiPersons.as_view(), name='persons'),
]
urlpatterns = help_patterns
