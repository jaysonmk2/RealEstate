from django.shortcuts import get_object_or_404, render
from .models import Homes

# Create your views here.
def properties(request):
    homes = Homes.objects.all()
    return render(request, 'properties/properties.html', {'homes' : homes})

def propertie_detail(request, homes_id):
    homes = get_object_or_404(Homes, pk = homes_id)
    return render(request, 'properties/detail.html', {'home': homes})
