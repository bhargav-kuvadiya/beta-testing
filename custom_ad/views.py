from django.shortcuts import render

# Create your views here.
def custom_ad_index(request):
    resp_dict = {
        'current_index': 'custom_ad'
    }
    return render(request, 'custom_ad/custom_ad_index.html', resp_dict)