from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect 

# Create your views here.

def index(request):
    return render(request, 'index.html', {'home': True})

def requirements(request):
    return render(request, "requirements.html")

@csrf_protect
def design_recommendations(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        data = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
        }

        return render(request, "design_recommendations.html", data)