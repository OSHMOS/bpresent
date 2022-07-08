from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import DetailView, CreateView, DeleteView
from attendance.models import Card, Name
from attendance.forms import NameForm

class NameDetailView(DetailView):
  model = Name
  pk_url_kwarg = 'name_id'


# class NameCreateView(LoginRequiredMixin, CreateView):
#   model = Name
#   form_class = NameForm

#   def form_valid(self, form):
#     form.instance.card = self.object.card
#     form.save()
#     return super().form_valid(form)

#   def get_success_url(self):
#     return reverse('card_detail', kwargs={'pk':self.object.id})


@login_required(login_url='account_login')
def name_create(request, pk):
  card = get_object_or_404(Card, id=pk)
  
  if request.method == "POST":
      form = NameForm(request.POST)
      if form.is_valid():
          name = form.save(commit=False)
          name.card = card
          name.save()
          return redirect('card_detail', pk)
  else:
    form = NameForm()

  return render(request, 'attendance/name_form.html', {'form':form})


@login_required(login_url='account_login')
def name_update(request, name_id):
  name = get_object_or_404(Name, id=name_id)
  
  if request.method == "POST":
      form = NameForm(request.POST, instance=name)
      if form.is_valid():
          name.save()
          return redirect('card_detail', pk=name.card.id)
  else:
      form = NameForm(instance=name)
  ctx = {'form' : form}
  return render(request, 'attendance/name_update_form.html', ctx)


class NameDeleteView(LoginRequiredMixin, DeleteView):
  model = Name
  pk_url_kwarg = 'name_id'

  def get_success_url(self):
    return reverse('card_detail', kwargs={"pk":self.object.card.id})


def name_attend(request,name_id):
  name = get_object_or_404(Name, id=name_id)
  name.dt_attend = timezone.now()
  name.save()
  return redirect('{}#name_{}'.format(
    resolve_url('card_detail', pk=name.card.id),name.id))


def name_late(request, name_id):
  name = get_object_or_404(Name, id=name_id)
  name.dt_attend = None
  name.dt_late = timezone.now()
  name.save()
  return redirect('{}#name_{}'.format(
    resolve_url('card_detail', pk=name.card.id),name.id))


def name_absent(request, name_id):
  name = get_object_or_404(Name, id=name_id)
  name.dt_attend = None
  name.dt_late = None
  name.dt_absent = timezone.now()
  name.save()
  return redirect('{}#name_{}'.format(
    resolve_url('card_detail', pk=name.card.id),name.id))