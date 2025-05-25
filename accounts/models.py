from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('athlete', 'Спортсмен'),
        ('coach', 'Тренер'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='athlete')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
