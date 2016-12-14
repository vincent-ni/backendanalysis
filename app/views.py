"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .forms import *

from .sql import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home',
            'year': datetime.now().year,
        }
    )

def analysisA(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    output = []
    is_found = False
    if request.method == "POST":
        box = NameBox(request.POST)
        data = request.POST.get('name')
	output = getBookStats(data)
        if not output:
            output = getBookList()
        else:
            is_found = True
    else:
        box = NameBox()
    return render(
        request,
        'app/analysis_a.html',
        {
            'box': box,
            'title': 'Analysis A',
            'year': datetime.now().year,
            'output': output,
            'found': is_found,
        }
    )

def analysisB(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    output = []
    is_found = False
    if request.method == "POST":
        nameBox = NameBox(request.POST)
        longBox = LongBox(request.POST)
        latBox = LatBox(request.POST)
        radiusBox = RadiusBox(request.POST)
        name = request.POST.get('name')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        radius = request.POST.get('radius')
        output = getLocationsNearby(name, longitude, latitude, radius)
        if not output:
            output = getBookList()
        else:
            is_found = True
    else:
        nameBox = NameBox()
        longBox = LongBox()
        latBox = LatBox()
        radiusBox = RadiusBox()
    return render(
        request,
        'app/analysis_b.html',
        {
            'nameBox': nameBox,
            'longBox': longBox,
            'latBox': latBox,
            'radiusBox': radiusBox,
            'title': 'Analysis B',
            'year': datetime.now().year,
            'output': output,
            'found': is_found,
        }
    )
