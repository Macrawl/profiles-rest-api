from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager 



class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email: 
            raise ValueError('user must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        #the set password function helps to encrypt the password 
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    #underneath the docstring, we specify the various fields we want to define in our model
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    #for staff i.e users with access to the Django admin 
    is_staff = models.BooleanField(default=False)
    #Create a model manager to be used for the objects to interact with the django Cli
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user """
        return self.name
   #The string representation of our model; the item we want to return when we convert a user profile to a string 
    def __str__(self):
        """ Return string representation of our user"""
        return self.email
    


