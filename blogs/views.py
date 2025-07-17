from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def article_list(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'blogs/my_articles.html', {'articles': articles})

@login_required
def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect('my_articles')
    return render(request, 'blogs/article_form.html', {'form': form})

@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('my_articles')
    return render(request, 'blogs/article_form.html', {'form': form})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    article.delete()
    return redirect('my_articles')