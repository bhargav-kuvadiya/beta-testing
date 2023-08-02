from django.shortcuts import render

# Create your views here.
def ep_index(request):
    resp_dict = {
        'current_index': 'ep'
    }
    return render(request, 'ep/ep_index.html', resp_dict)