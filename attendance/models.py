from django.db import models
from common.models import User
# Create your models here.
class Card(models.Model):
  title = models.CharField(max_length=100, verbose_name="제목")
  manager = models.ForeignKey(User, on_delete=models.CASCADE)
  dt_created = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.title


class Name(models.Model):
  name = models.CharField(max_length=10, verbose_name="이름")
  card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
  dt_attend = models.DateTimeField(null=True, blank=True)
  dt_late = models.DateTimeField(null=True, blank=True)
  dt_absent = models.DateTimeField(null=True, blank=True)

  def __str__(self):
      return self.name
  