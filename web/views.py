import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import UpdateView

from .models import Blog, Blogger, Comment
from .forms import CommentForm
# Lembrar de adicionar o derocador loginrequired.

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


# class CommentCreateView(LoginRequiredMixin, generic.CreateView):
#     # model = Blog.comments.through
#     # queryset = Blog.comments
#     model = Comment
#     # fields = ['comments']
#     # model = Blog
#     fields = ['comment_author', 'commentary']
#     initial = {'comment_author': 'request.user'}
#     template_name = 'web/comment_form.html'
#     # success_url = reverse_lazy('blog_detail')
#
#     # def get_context_data(self, **kwargs):
#     #     pass


# (falta acrestentar a edição/remoção de comentários <-- OK) + página de cadastro de usuário
def add_commentary(request, slug):
    """View function para a página de adicionar comentários"""
    blog = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        data = {
            # 'comment_date': datetime.datetime.now(),
            'commentary': request.POST['commentary']
        }

        form = CommentForm(data)
        # print(form, 'if')
        if form.is_valid():
            blog.comments.create(
                comment_author=request.user,
                comment_date=datetime.datetime.now(),
                commentary=form.cleaned_data['commentary']
            )
            # comment.comment_author = form.cleaned_data['comment_author']
            # comment.comment_author = request.user # desta maneira os comentários são editados
            # comment.comment_date = form.cleaned_data['comment_date'] # desta maneira os comentários são editados
            # comment.commentary = form.cleaned_data['commentary'] # desta maneira os comentários são editados
            # print(form.comment_date)
            # blog.comments = form.cleaned_data[data]
            # blog.save()
            # comment.save() # desta maneira os comentários são editados
            return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))

    else:
        # print(form)
        # Se a requisição for diferente de POST, será renderizado um formulário vazio:
        form = CommentForm()
        # print(form, 'else')

    context = {
        'form': form,
        'blog': blog
    }

    return render(request, 'web/comment_form.html', context)


def edit_commentary(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    comment_id = request.GET.get('c_id')
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        data = {
            'commentary': request.POST['commentary']
        }
        form = CommentForm(data)
        
        if form.is_valid():
            comment.commentary = form.cleaned_data['commentary']
            comment.save()

            return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))

    else:
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

# class CommentUpdate(UpdateView):
#     # model = Comment
#     queryset = get_object_or_404(Blog, slug=request.slug)
#     slug = Blog.slug
#     slug_url_kwarg = slug
#     template_name = 'web/comment_form.html'


def remove_commentary(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comment_id = request.GET.get('c_id')
    comment = Comment.objects.get(id=comment_id)
    
    print(comment_id)
    print(comment)
    
    if request.method == 'POST':
        comment.delete()
        # comment.save()

        return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))

    else:
        return render(request, 'web/comment_confirm_delete.html')
    
        # return HttpResponseRedirect(reverse('blog_detail', args=(blog.slug,)))
