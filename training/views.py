from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@login_required
def index(request):
    return render(request, 'training/index.html',)
