from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,UserManager

class CustomUserManager(UserManager):
    # custom manager methods here
    
    def create_user(self, username,  email, first_name, last_name, phone_number, address, password):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not address:
            raise ValueError('Users must have an address')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, first_name, last_name, phone_number, address, password, is_staff=True, is_superuser=True):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    # custom user  fields are phone and address
    username=models.CharField(max_length=255,blank=True,unique=True,default='')
    first_name = models.CharField(max_length=255 ,blank=False,default='')
    last_name = models.CharField(max_length=255, blank=False,default='')
    email = models.EmailField(max_length=255, unique=True,blank=False)
    password = models.CharField(max_length=255,blank=False)
    phone_number = models.CharField(max_length=20,blank=False,default='')
    address = models.CharField(max_length=100,blank=False,default='')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
        
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name', 'email', 'phone_number', 'address']
    
