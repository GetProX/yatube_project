from django.shortcuts import render, get_object_or_404

from .models import Group, Post

from django.conf import settings


def index(request):
    posts = Post.objects.select_related('group', 'author')[:settings.NUM_POST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    # Загружаем посты группы;
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.NUM_POST]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
