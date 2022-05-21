from django.shortcuts import render

def index(request):
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):

    return render(request, 'posts/group_list.html')
