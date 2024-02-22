from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'HOD'),
        ('staff_user', 'Staff'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=15, choices=ROLES, blank=True, null=True)
    
    def is_staff_or_superuser(self):
        return self.is_superuser or self.role == 'staff_user'