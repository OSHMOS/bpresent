from django.db import models
from common.models import User
# Create your models here.
class Card(models.Model):
  manager = models.ForeignKey(User, on_delete=models.CASCADE)
  dt_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"{self.manager} : {self.dt_created}"


class NameList(models.Model):
  name = models.CharField(max_length=10)

  def __str__(self):
      return self.name
  