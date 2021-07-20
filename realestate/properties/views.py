from django.shortcuts import render
from .models import Homes

# Create your views here.
def properties(request):
    homes = Homes.objects.all()
    return render(request, 'properties.html', {'homes' : homes})