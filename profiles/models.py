from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

from .utils import generate_account_number

# Create your models here.


class Profile(models.Model):
    """
    Class for the owner of the invoice
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=26, blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(default='images/avatar.png')
    company_logo = models.ImageField(default='images/no_photo.png')

    def __str__(self):
        return f"Profile of the user: {self.user.username}"

    def save(self, *args, **kwargs):
        if self.account_number == "":
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

    # def clean(self):
    #     if len(self.account_number) != 26:
    #         raise ValidationError('Bank account number must be 26 characters long')
