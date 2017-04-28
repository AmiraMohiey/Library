from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import JsonResponse, HttpResponse, Http404
from django.views.generic import View, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Category, Book, Author
from django.core import serializers
from django import template



class Home(View):
    template_name = "home.html"

    def get(self, request):
        if request.user.is_authenticated():
            last_five_books = Book.objects.all().order_by('-id')[:5]
            category = Category.objects.filter(users=request.user)
            return render(request, 'home.html', context={"category": category, "latestbooks": last_five_books})
        else:
            return redirect('login')


class CategoryDetails(generic.DetailView):
    model = Category

    def get(self, request, pk):

        books = Book.objects.filter(category_id=pk)

        try:
            category = Category.objects.get(pk=pk)
            users = User.objects.all().filter(category=category)

        except Category.DoesNotExist:
            raise Http404("Category does not exist")
        return render(request, 'categorydetails.html', context={"category": category, "users": users, "books": books})

    def post(self, request, pk):
        print("post", pk)

        category = Category.objects.get(pk=pk)
        category.users.add(request.user)
        users = User.objects.all().filter(category=category)
        return render(request, 'categorydetails.html', context={"category": category, "users": users})


class RemoveFromFavourites(View):
    def post(self, request):
        pk = request.POST.get('pk')
        category = Category.objects.get(pk=pk)
        category.users.remove(request.user)

        print(pk)
        users = User.objects.all().filter(category=category)
        return redirect('/categorydetails/' + pk, context={"category": category, "users": users})


class CategoryList(generic.ListView):
    model = Category

    def get(self, request):
        print("category")
        category = Category.objects.all()
        # return render(request, 'header.html', context={"categories": category})
        json_data = serializers.serialize('json', category)
        return HttpResponse(json_data)


class Header(generic.View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'header.html', context={"categories": category})


class AuthorsList(generic.ListView):
    template_name = 'authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetails(generic.DetailView):
    model = Author
    template_name = 'authordetails.html'


class BooksList(generic.ListView):
    template_name = 'books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()

class BookDetails(generic.DetailView):
    model = Book
    template_name = 'bookdetails.html'

class Search(View):
    def post(self, request):
        search_query = request.POST.get('search_query')
        qset_book = Q()
        qset_author = Q()
        for term in search_query.split():
            qset_book |= Q(title__icontains=term)

        books = Book.objects.filter(qset_book)
        for term in search_query.split():
            qset_author |= Q(name__icontains=term)
        authors = Author.objects.filter(qset_author)
        return render(request, 'searchresults.html', context={"books": books, "authors": authors})

    def get(self, request, search_query):
        qset_book = Q()
        qset_author = Q()
        for term in search_query.split():
            qset_book |= Q(title__icontains=term)

        books = Book.objects.filter(qset_book)
        for term in search_query.split():
            qset_author |= Q(name__icontains=term)
        authors = Author.objects.filter(qset_author)

        print(search_query)

        json_books = serializers.serialize('json', books)
        json_authors = serializers.serialize('json', authors)
        return JsonResponse(json_books, safe=False)


