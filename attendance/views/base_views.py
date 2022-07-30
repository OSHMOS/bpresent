from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from attendance.models import Bookmark

def index(request):
  return render(request, 'attendance/index.html')


def how(request):
  return render(request, 'attendance/how.html')


def privacy(request):
  return render(request, 'account/privacy.html')


@login_required(login_url = 'account_login')
def profile(request):
  bookmark_list = Bookmark.objects.all()
  ctx = {'bookmark_list': bookmark_list}
  return render(request, 'account/profile.html', ctx)