from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  # 最初から設定すると変更できなくなる
  name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  department = models.CharField(max_length=100, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return f"{self.name} ({self.user.username if self.user else 'No User'})"
