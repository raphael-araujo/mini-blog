from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_blogs/', views.BlogsListView.as_view(), name='all_blogs'),
    path('all_bloggers/', views.BloggersListView.as_view(), name='all_bloggers'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blogger/<slug:slug>', views.BloggerDetailView.as_view(), name='blogger_detail'),
    path('<slug:slug>/add_comment/', views.comment_page, name='comment_create'),
]
