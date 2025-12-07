# tracking/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def location_view(request):
    return render(request, 'tracking/location.html')