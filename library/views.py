from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View, DetailView
from .models import Category
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse,Http404

from django.core import serializers
class Home(View):
    template_name = "home.html"

    def get(self, request):
        if request.user.is_authenticated():
            category = Category.objects.filter(users=request.user)
            return render(request, 'home.html',context={"category":category})
        else:
            return redirect('login')


class CategoryDetails(generic.DetailView):
    model = Category
    def get(self, request, pk):

        # books = Book.objects.filter(category_id=cat_id)

        try:
            category= Category.objects.get(pk=pk)

            users=User.objects.all().filter(category=category)
            print(category)
            print(users)

        except Category.DoesNotExist:
            raise Http404("Category does not exist")

        return render(request, 'categorydetails.html', context={"category": category, "users": users})


class CategoryList(generic.ListView):
    model = Category

    def get(self, request):
        print("category")
        category = Category.objects.all()
        # return render(request, 'header.html', context={"categories": category})
        json_data = serializers.serialize('json', category)
        return HttpResponse(json_data)




        # return render(request, 'categorydetails.html', context={"category": category})