from django.shortcuts import render
from django.views import generic

from .models import Blog, Blogger, Comment

# Create your views here.


def index(request):
    """
    Página inicial
    """
    
    # Para contar o número de blogs:
    num_blogs = Blog.objects.all().count()
    
    # Para contar o número de autores:
    num_bloggers = Blogger.objects.all().count()
    
    # Número de visitas para esta view (é contado na variável session):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits
    }
    
    return render(request, 'index.html', context)


class BlogsListView(generic.ListView):
    """class-based view que lista os blogs"""
    model = Blog
    ordering = ['-post_date']  # Ordena a lista por data de postagem (mais recente).
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    """class-based view que mostra os detalhes de um blog"""
    model = Blog


class BloggersListView(generic.ListView):
    """class-based view que lista os blogueiros"""
    model = Blogger
    ordering = ['first_name']  # Ordena a lista por ordem alfabética.
    paginate_by = 5


class BloggerDetailView(generic.DetailView):
    """class-based view que mostra os detalhes de um blogueiro"""
    model = Blogger
    