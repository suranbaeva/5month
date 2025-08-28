from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False, null=True, blank=True)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_confirmation_code(self, *args, **kwargs):
        if not self.confirmation_code:
            code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            self.confirmation_code = code  # ЭТОГО НЕ ХВАТАЕТ
        super().save(*args, **kwargs)



