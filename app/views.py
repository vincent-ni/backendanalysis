"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .forms import TextBox

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
        box = TextBox(request.POST)
        data = request.POST.get('query')
	output = getBookStats(data)
        if not output:
            output = getBookList()
        else:
            is_found = True
    else:
        box = TextBox()
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
        box = TextBox(request.POST)
        data = request.POST.get('query')
        output = getBookStats(data)
        if not output:
            output = getBookList()
        else:
            is_found = True
    else:
        box = TextBox()
    return render(
        request,
        'app/analysis_b.html',
        {
            'box': box,
            'title': 'Analysis B',
            'year': datetime.now().year,
            'output': output,
            'found': is_found,
        }
    )
