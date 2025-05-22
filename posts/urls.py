from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path, include
from . import views 
app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('post-detail/<int:pk>/', views.post_details, name='post_details'),
    path('post/create_comment/<int:id>/', views.comment, name='create_comment'),
    path('post/category/<int:pk>/', views.category, name='category'),
    path('post/tags/<int:pk>/', views.filter_tag, name='filter_tags'),
    path('search/', views.search, name='search'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)