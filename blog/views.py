from django.shortcuts import render

# Create your views here.
def blog_index(request):
    resp_dict = {
        'current_index': 'blog'
    }
    return render(request, 'blog/blog_index.html', resp_dict)