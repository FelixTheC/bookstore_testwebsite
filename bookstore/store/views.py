from .models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, ListView


class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    ordering = 'title'

    def get_queryset(self, **kwargs):
        return super(BookListView, self).get_queryset(**kwargs).all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        return super(BookDetailView, self).get_context_data(**kwargs)


def bookDetail(request, pk):
    book = Book.objects.filter(pk=pk)
    context = {
        'book': book
    }
    return render(request, template_name='detail.html', context=context)