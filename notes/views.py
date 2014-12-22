from django.shortcuts import render, HttpResponse

# Create your views here.

class home_page(request):
    return render(request, 'home.html', locals())