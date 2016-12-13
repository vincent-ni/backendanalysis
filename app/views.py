"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .forms import TextBox

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
    if request.method == "POST":
        box = TextBox(request.POST)
        data = request.POST.get('query')
    else:
        box = TextBox()
    return render(
        request,
        'app/a.html',
        {
            'box': box,
            'title': 'Analysis A',
            'year': datetime.now().year,
        }
    )

def analysisB(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        box = TextBox(request.POST)
        data = request.POST.get('query')
    else:
        box = TextBox()
    return render(
        request,
        'app/b.html',
        {
            'box': box,
            'title': 'Analysis B',
            'year': datetime.now().year,
        }
    )
