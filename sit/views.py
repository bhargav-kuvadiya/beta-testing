from django.shortcuts import render

# Create your views here.
def sit_index(request):
    resp_dict = {
        'current_index': 'sit'
    }
    return render(request, 'sit/sit_index.html', resp_dict)