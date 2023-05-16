from django.shortcuts import render

# Create your views here.

def requirements(request):
    return render(request, "obrasnet/templates/requirements.html")
