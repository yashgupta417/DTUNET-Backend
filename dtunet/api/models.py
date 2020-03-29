from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
import uuid

#https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
class UserManager(BaseUserManager):
    #however, if your user model defines different fields, you’ll need to define
    #a custom manager that extends BaseUserManager providing two additional methods:
    #create_user() and create_superuser()

    def create_user(self, email, password=None):
        """Creates and saves a User with the given email and password."""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a superuser with the given email and password."""
        user = self.create_user(email,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

#https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
class User(AbstractBaseUser):
    u_id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True,max_length=255,null=False,blank=False)
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    label=models.CharField(max_length=255,null=True,blank=True) #student,alumni,faculty,society
    bio=models.CharField(max_length=255,null=True,blank=True)
    is_online=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)#using admin flag instead of permission mixin
    following=models.ManyToManyField('User',related_name='followers',blank=True)
    #"Password field" is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    objects = UserManager()

    def __str__(self):
        return self.email

    ##If you want your custom user model to also work with the admin, your user model must define following attributes and methods
    is_active=models.BooleanField(default=True)

    @property
    def is_staff(self):
        """Is the user a member of staff?"""# Simplest possible answer: All admins are staff
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `api`?"""
        return True
