
from django.conf.urls import url
from django.contrib import admin
from users import views
from library import views as library_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', library_views.Header.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^register/',views.UserRegisterationView.as_view(),name='register'),
    url(r'^login/',views.UserLoginView.as_view(),name='login'),
    url(r'^logout/', views.UserLogout.as_view(), name='logout'),
    url(r'^home/', library_views.Home.as_view(), name='home'),
    url(r'^categorydetails/(?P<pk>[0-9]+)/', library_views.CategoryDetails.as_view(), name='categorydetails'),
    url(r'^categorylist/', library_views.CategoryList.as_view(), name='categorylist'),
    url(r'^authors/', library_views.AuthorsList.as_view(), name='authors_list'),
    url(r'^author/(?P<pk>[0-9]+)/', library_views.AuthorDetails.as_view(), name='author'),
    url(r'^books/', library_views.BooksList.as_view(), name='books_list'),
    url(r'^book/(?P<pk>[0-9]+)/', library_views.BookDetails.as_view(), name='book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
