import random
import string
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models


class ClientManager(BaseUserManager):
    def create_client(self, first_name, last_name, username, email, is_active, joined, phone_number, email_confirm_key, key_expires, password):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            is_active=is_active,
            joined=joined,
            phone_number=phone_number,
            email_confirm_key=email_confirm_key,
            key_expires=key_expires,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, is_active, joined, phone_number, email_confirm_key, key_expires, password):

        user = self.create_user(email,
                                last_name=last_name,
                                username=username,
                                is_active=is_active,
                                joined=joined,
                                phone_number=phone_number,
                                email_confirm_key=email_confirm_key,
                                key_expires=key_expires
                                )

        user.is_admin = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):
    # user = models.OneToOneField
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    username = models.CharField('username', max_length=30, unique=True)
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=13)
    email_confirm_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    objects = ClientManager()
    def __unicode__(self):
        return self.email


class SendSMS(models.Model):
    to_number = models.CharField(max_length=30)
    from_number = models.CharField(max_length=30)
    sms_sid = models.CharField(max_length=34, default="", blank=True)
    account_sid = models.CharField(max_length=34, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="", blank=True)