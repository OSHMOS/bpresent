import requests
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bs4 import BeautifulSoup
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
        return reverse('card_detail', kwargs={'pk': self.object.id})


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card

    def get_success_url(self):
        return reverse('card_list')


@login_required(login_url='account_login')
def card_to_csv(request, pk):
    session = requests.session()
    # beautifulsoup을 활용하여 자동으로 로그인이 되게 해야 한다.
    data = {
        'return_url': 'https://bpresent.kr/'
    }
    url = f'https://bpresent.kr/detail/{pk}'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # title = soup.find_all('span')
    # name = soup.find_all('h3', 'name')
    # status = soup.find_all('h3', 'status')
    # print(title)
    # print(name)
    # print(status)
    return redirect('card_detail', pk)
