
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View,DetailView
from .models import Category



# Create your views here.

class Home(View):
    template_name = "home.html"
    def get(self, request):
            if request.user.is_authenticated():
                return render(request, 'home.html')
            else:
                return redirect('login')

class CategoryDetails(DetailView):
    model= Category
    
    def get(self,request,pk):
        category = Category.objects.filter(id=pk)
        # b = Book.objects.filter(category_id=cat_id)

        return render(request, 'categorydetails.html', context={"category": category, "books": "book"})
