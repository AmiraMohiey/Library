from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Book,Category,Author
import sys

# ------------------Testing Models-------------------------

class test_category_model(TestCase):
    def create_Category(self, name="only a test"):
        return Category.objects.create(name=name)
    def test_category_creation(self):
        w = self.create_Category()
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w.__str__(), w.name)

class test_author_model(TestCase):
    def create_Author(self, name="only a test"):
            return Author.objects.create(name=name)
    def test_author_creation(self):
            w = self.create_Author()
            self.assertTrue(isinstance(w, Author))
            self.assertEqual(w.__str__(), w.name)

#------------------Testing Views----------------------------

class test_book_list(TestCase):
    def test_book_list_view(self):
        url = reverse("books_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

class test_author_view(TestCase):
    def test_author_list_view(self):
        url = reverse("authors_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
class test_home_view(TestCase):
    def test_home_view(self):
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)







