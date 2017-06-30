from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from .views import BookDetailView, BookListView

app_name = 'store'
urlpatterns = [
    url(r'^$', BookListView.as_view(), name='book_main'),
    url(r'^book/(?P<pk>[\d]+)/$', BookDetailView.as_view(), name='bookDetail'),
]