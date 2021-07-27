from django.shortcuts import render

posts = [
    {
        'author': 'ahmed',
        'date_posted': '15/10/2020',
        'title': 'django rest',
        'content': 'this is a content for the django rest framework'
    },
    {
        'author': 'yossf',
        'date_posted': '20/6/2021',
        'title': 'react native',
        'content': 'this is a content for the react native cross platform framework'
    },
    {
        'author': 'hady',
        'date_posted': '16/5/2019',
        'title': 'flutter',
        'content': 'this is a content for flutter'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
    
def about(request):
    return render(request, 'blog/about.html', {"title":"about"})
