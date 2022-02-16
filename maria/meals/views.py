from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
import datetime
from . import models

def index(request):
    return HttpResponse("Hello world. This is the maria index.")

class MealListView(ListView):
    
    model = models.Meal
    template_name = 'meal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class MealDetailView(DetailView):

    model = models.Meal
    template_name = 'meal_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class MealCreateView(PermissionRequiredMixin, CreateView):
    model = models.Meal
    fields = '__all__'
    initial = {
        'name': 'name'
    }
    permission_required = 'meals.is_admin'

def MealUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Meal
    fields = '__all__' #changeme
    premission_required = 'meals.is_admin'

def MealDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Meal
    success_url = reverse_lazy('meals')
    permission_required = 'meals.is_admin'