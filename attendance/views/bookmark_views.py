from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from attendance.models import Card, Name, Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from attendance.forms import BookmarkForm


# @login_required(login_url='account_login')
# def bookmark_create(request, pk):
#     card = get_object_or_404(Card, id=pk)
#     bookmark = get_object_or_404(Bookmark, id=pk)

#     if bookmark in card.bookmark.all:
#         print('이미 즐겨찾기가 있습니다.')

#     if request.method == 'POST':
#         form = BookmarkForm(request.POST)
#         if form.is_valid():
#             bookmark = form.save(commit=False)
#             bookmark.card = card
#             bookmark.save()
#             return redirect('profile')
#     else:
#         form = BookmarkForm()
#     ctx = {'form': form, 'card': card}
#     return render(request, 'attendance/bookmark_form.html', ctx)


# @login_required(login_url='account_login')
# def bookmark_update(request, pk):
#     pass
