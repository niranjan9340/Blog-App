from django.urls import path,include
from django.contrib.auth import urls
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('post/<slug:slug>', views.post_page, name="post_page"),
    path('tag/<slug:slug>', views.tag_page, name="tag_page"),
    path('author/<slug:slug>', views.author_page, name="author_page"),
    path('search/', views.search_posts, name="search"),
    path('about/', views.about, name="about"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register_user, name="register"),
    path('bookmark_post/<slug:slug>', views.bookmark_post, name="bookmark_post"),
    path('like_post/<slug:slug>', views.like_post, name="like_post"),
    path('all_bookmarked_posts/', views.all_bookmarked_posts, name="all_bookmarked_posts"),
    path('all_posts/', views.all_posts, name="all_posts"),
    path('all_liked_post/', views.all_liked_post, name="all_liked_post"),
]
