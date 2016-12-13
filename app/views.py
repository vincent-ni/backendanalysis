"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from .forms import TextBox

from .sql import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
    )

def analysisA(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        box = TextBox(request.POST)
        data = request.POST.get('query')
	output = getBookStats(data)
	print output
    else:
        box = TextBox()
    return render(
        request,
        'app/a.html',
        {'box': box}
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
        {'box': box}
    )
