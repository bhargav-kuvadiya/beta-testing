from django.shortcuts import render

# Create your views here.
def projects_index(request):
    resp_dict = {
        'current_index': 'projects'
    }
    return render(request, 'projects/projects_index.html', resp_dict)