from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from attendance.models import Card, Name
from attendance.forms import CardForm, NameForm

# Create your views here.


class CardListView(LoginRequiredMixin, ListView):
    model = Card


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = "attendance/name_list.html"


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card_list')


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'attendance/card_update_form.html'

    def get_success_url(self):
        return reverse('card_list')


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card

    def get_success_url(self):
        return reverse('card_list')
