from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView
from django.views.generic import TemplateView

import user
from api.models import *


class HomeView(ListView):
    context_object_name = "contacts"
    template_name = 'user/home.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Person.objects.filter(id__lte = 100)
        return None

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class AddMember(CreateView):
    model = Person
    template_name = 'user/add_member.html'
    fields = '__all__'


