from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .form import RegisterationForm
from .form import LoginForm



class UserRegisterationView(View):
    form_class = RegisterationForm
    template_name = "register.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request, self.template_name,
                          {"form": form, "error": "you entered invalid format please try again"})


class UserLoginView(View):
    form_class = LoginForm
    template_name = "login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
         form = self.form_class(request.POST)
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(username=username, password=password)

         if user is not None:
                login(request, user)
                return redirect('home')
         else:
                return render(request, self.template_name, {"form": form, "error": "Invalid Login"})


         return render(request, self.template_name, {"form": form, "error": "Invalid Logins"})




class UserLogout(View):

    def get(self, request):
            if request.user.is_authenticated():
               logout(request)
               redirect('login')
            return redirect('login')



