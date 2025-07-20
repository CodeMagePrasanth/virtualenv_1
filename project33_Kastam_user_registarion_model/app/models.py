from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserProfileManagar(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('please provide email')
        NE=self.normailse_email(email)
        UO = self.model(email=NE,first_name=first_name,last_name=last_name)  # model- is objects of UserPrfile
        UO.set_password(password)
        UO.save()
        return UO
    
    def create_superuser(self,email,first_name,last_name,password):
        UO = self.create_user(email,first_name,last_name,password)
        UO.is_staff=True
        UO.is_superuser=True
        UO.save()

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email= models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    # password filed is not mandatory that done py Abstractbaseuser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # this my authentication filed
    REQUIRED_FIELDS =['first_name','last_name'] # what ever uou make requirued filed

    objects=UserProfileManagar() # it make connection to UserProfileManager and the addres store in model variable
    