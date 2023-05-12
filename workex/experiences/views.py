from django.shortcuts import render
from .models import Experience
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def experiences_list(request):
    experiences = Experience()
    return render(request, 'experiences/experience_list.html', {'experiences': experiences})


def experience_detail(request, pk):
    experience = Experience.get_constraints(pk)
    return render(request, 'experiences/experience_detail.html', {'experience': experience})


@login_required
class ExperienceCreate(LoginRequiredMixin, CreateView):
    model = Experience
    fields = ['title', 'description', 'image', 'video']
    success_url = reverse_lazy('experience_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
