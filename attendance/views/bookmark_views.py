from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from attendance.models import Card, Name, Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from attendance.forms import BookmarkForm

# class BookmarkCreateView(LoginRequiredMixin, CreateView):
#     model = Bookmark
#     form_class = BookmarkForm()

#     def form_valid(self, form):
#         form.instance.card = self.objects.card
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('card_list')


@login_required(login_url='account_login')
def bookmark_save(request, pk):
  card = get_object_or_404(Card, id=pk)
  if request.method == 'POST':
    form = BookmarkForm(request.POST)
    if form.is_valid():
      bookmark = form.save(commit=False)
      bookmark.card = card
      bookmark.save()
      return redirect('profile')
  else:
    form = BookmarkForm()
  ctx = {'form': form, 'card': card}
  return render(request, 'attendance/bookmark_form.html', ctx)


@login_required(login_url='account_login')
def bookmark_load(request, bookmark_id):
  pass