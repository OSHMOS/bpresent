from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
  return render(request, 'attendance/index.html')


def privacy(request):
  return render(request, 'account/privacy.html')


@login_required(login_url = 'account_login')
def profile(request):
  return render(request, 'account/profile.html')