
from django.conf.urls import url
from django.contrib import admin
from users import views
from library import views as library_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/',views.UserRegisterationView.as_view(),name='register'),
    url(r'^login/',views.UserLoginView.as_view(),name='login'),
    url(r'^logout/', views.UserLogout.as_view(), name='logout'),
    url(r'^home/', library_views.Home.as_view(), name='home'),
    url(r'^category/(?P<pk>\d+)', library_views.Home.as_view(), name='category'),
]
