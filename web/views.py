import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .forms import CommentForm
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

    # Ordena a lista por data de postagem (mais recente):
    ordering = ['-post_date']
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


@login_required(login_url='/auth/login')
def add_commentary(request, slug):
    """View function para a página de adicionar comentários"""

    blog = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        data = {
            'commentary': request.POST['commentary']
        }
        form = CommentForm(data)

        # Se os dados forem válidos, será criado um novo comentário:
        if form.is_valid():
            blog.comments.create(
                comment_author=request.user,
                comment_date=datetime.datetime.now(),
                commentary=form.cleaned_data['commentary']
            )
            # Depois o usuário será redirecionado novamente para o blog em que estava:
            return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))

    else:
        # Se a requisição for diferente de POST, será renderizado um formulário vazio:
        form = CommentForm()

    context = {
        'form': form,
        'blog': blog
    }

    return render(request, 'web/comment_form.html', context)


@login_required(login_url='/auth/login')
def edit_commentary(request, slug):
    """View function para editar comentários."""

    blog = get_object_or_404(Blog, slug=slug)

    # Buscar no banco de dados o comentário com o mesmo id da requisição 'get':
    comment_id = request.GET.get('c_id')
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        data = {
            'commentary': request.POST['commentary']
        }
        form = CommentForm(data)

        # Se o formulário estiver válido, o comentário antigo será substituído pelo novo:
        if form.is_valid():
            comment.commentary = form.cleaned_data['commentary']
            comment.save()

            # Após a edição, o usuário será redirecionado para o blog em que estava:
            return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))

    else:
        # Será renderizado um comentário inicialmente preenchido, para o usuário fazer a edição:
        form = CommentForm(
            initial={
                'commentary': comment.commentary
            }
        )
        context = {
            'blog': blog,
            'form': form
        }
        return render(request, 'web/comment_form.html', context)


@login_required(login_url='/auth/login')
def remove_commentary(request, slug):
    """View function para remover comentários."""

    blog = get_object_or_404(Blog, slug=slug)
    comment_id = request.GET.get('c_id')
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        # O comentário será deletado:
        comment.delete()

        # O usuário vai ser redirecionado para o blog em que estava:
        return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))

    else:
        # Uma página de confirmação de exclusão será renderizada:
        return render(request, 'web/comment_confirm_delete.html')
