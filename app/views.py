"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest

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
    return render(
        request,
        'app/a.html',
    )

def analysisB(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/b.html',
    )
