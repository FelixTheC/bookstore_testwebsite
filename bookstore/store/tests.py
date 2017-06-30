from django.test import TestCase
from .models import Book

# Create your tests here.
class StoreTest(TestCase):
    def setUp(self):
        mybook = Book.objects.create(title='MyBook', author='Felix', description='Only a test not for public',
                                     price=12.95, stock=100)

    def test_book_exists(self):
        loadBook = Book.objects.get(title='MyBook')
        self.assertTrue(loadBook)

    def test_fail_update(self):
        theBook = Book.objects.create(title='NewBook', author='Felix')
        self.assertFalse(theBook)
