from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.user.email

        super().save(*args, **kwargs)