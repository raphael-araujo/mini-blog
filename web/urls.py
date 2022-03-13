from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_blogs/', views.BlogsListView.as_view(), name='all_blogs'),
    path('all_bloggers/', views.BloggersListView.as_view(), name='all_bloggers')
]
