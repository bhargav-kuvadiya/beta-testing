from django.shortcuts import render

# Create your views here.
def dashboard_index(request):
    resp_dict = {
        'current_index': 'dashboard'
    }
    return render(request, 'dashboard/dashboard_index.html', resp_dict)