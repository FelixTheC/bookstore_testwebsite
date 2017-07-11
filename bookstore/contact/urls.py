from django.conf.urls import url
from .views import ContactFormView

app_name = 'contact'
urlpatterns = [
    url(r'^mail/$', ContactFormView.as_view(), name='contact')
]