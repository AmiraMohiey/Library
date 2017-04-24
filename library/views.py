from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View, DetailView
from .models import Category
from django.http import JsonResponse,HttpResponse
import json
from django.core import serializers
class Home(View):
    template_name = "home.html"

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'home.html')
        else:
            return redirect('login')


class CategoryDetails(generic.DetailView):
    model = Category
    def get(self, request, pk):
        category = Category.objects.filter(id=pk)
      # books = Book.objects.filter(category_id=cat_id)
        return render(request, 'categorydetails.html', context={"category": category, "books": "books"})


class CategoryList(generic.ListView):
    model = Category

    def get(self, request):
        print("category")
        category = Category.objects.all()
        # return render(request, 'header.html', context={"categories": category})
        json_data = serializers.serialize('json', category)
        return HttpResponse(json_data)