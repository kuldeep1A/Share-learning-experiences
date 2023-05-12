from django.shortcuts import render
from .models import Experience


def experiences_list(request):
    experiences = Experience()
    return render(request, 'experiences/experience_list.html', {'experiences': experiences})


def experience_detail(request, pk):
    experience = Experience.get_constraints(pk)
    return render(request, 'experiences/experience_detail.html', {'experience': experience})
