from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create a new Requirement for url '/requirements'
## In this, client makes a reqruirement for the design.

@login_required
def requirements(request):
    return render(request, "requirements.html")