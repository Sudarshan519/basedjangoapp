# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from streaming_app.models import *
User = settings.AUTH_USER_MODEL
# users/models.py
from django.contrib.auth.base_user import BaseUserManager
# class Employer(AbstractUser):
#     phone=models.IntegerField()
#     is_verified=models.BooleanField(default=False)
class Employer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_verified=models.BooleanField(default=False)
    
    
class Customer(models.Model):
    """ Customer-specific information """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # businesses = models.ManyToManyField(Business)

class Employee(models.Model):
    """ Employee-specific information """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # business = models.ForeignKey(Business)

# class Business(models.Model):
#     business_name = models.CharField(max_length=50)
# class CustomUserManager(BaseUserManager):

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError("The given email must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(
#                 "Superuser must have is_staff=True."
#             )
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(
#                 "Superuser must have is_superuser=True."
#             )

#         return self._create_user(email, password, **extra_fields)
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    counter = models.IntegerField(default=0, blank=False)
    email_verified=models.BooleanField(blank=False,default=False)
    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    def movies(self):
        return Movie.objects.all()
    def tvshows(self):
        return TVSeries.objects.all()
#     objects = CustomUserManager()
# class User(AbstractUser):
    
    #   EMPLOYER = 1
    #   EMPLOYEE = 2
    #   APPROVER =3
      
    #   ROLE_CHOICES = (
    #       (EMPLOYER, 'Employer'),
    #       (EMPLOYEE, 'Employee'),
    #       (APPROVER, 'Approver'),
    #   )
    #   role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
      # You can create Role model separately and add ManyToMany if user has more than one role

# from django.contrib.auth.decorators import permission_required@permission_required('poll.add_vote') 
# def your_func(request):
#     """or you can rise permission denied exception"""  
# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.views.generic import ListViewclass VoteListView(PermissionRequiredMixin, ListView):
#     permission_required = 'polls.add_vote'
#     # Or multiple of permissions
#     permission_required = ('poll.add_vote', 'poll.change_vote')


# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType

# content_type = ContentType.objects.get_for_model(Vote)permission = Permission.objects.create(
#    codename='can_see_vote_count',
#    name='Can See Vote Count',
#    content_type=content_type,
# )

# Create Groups

# from django.contrib.auth.models import Groupdoctor_group, created = Group.objects.get_or_create(name='Doctor')

# 
# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType

# content_type = ContentType.objects.get_for_model(Vote)permission = Permission.objects.create(
#    codename='can_see_vote_count',
#    name='Can See Vote Count',
#    content_type=content_type,
# )


# Assign a user to groups

# doctor_group.user_set.add(user)
#             OR
# user.groups.add(doctor_group)

# Check user in the group

# def is_doctor(user):
#     return user.groups.filter(name='Doctor').exists()from django.contrib.auth.decorators import user_passes_test@user_passes_test(is_doctor)
# def my_view(request):
#     pass
 