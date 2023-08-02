from django.shortcuts import render

# Create your views here.
def it_index(request):
    resp_dict = {
        'current_index': 'it'
    }
    return render(request, 'it/it_index.html', resp_dict)