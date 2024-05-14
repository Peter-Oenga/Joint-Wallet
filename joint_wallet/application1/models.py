from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None, phone_number=None):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")
        if not email and not phone_number:
            raise ValueError("Users must have an email address or phone number")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email) if email else None,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None, email=None, phone_number=None):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            phone_number=phone_number,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']
    
    def __str__(self):
        return self.username
