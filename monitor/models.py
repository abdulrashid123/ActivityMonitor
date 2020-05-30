# import require libraries containing inbuilt user model also
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Override User model


class MyActivityManager(BaseUserManager):
    def create_user(self,id,username, password, timezone):
        user = self.model(real_name = username)
        user.id = id
        user.tz = timezone
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,password):
        user = self.create_user(username=username)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser):
    id = models.CharField(max_length=2000,primary_key=True)
    real_name = models.CharField(max_length=2000,unique=True)
    password = models.CharField(max_length=2000)
    tz = models.CharField(max_length=2000)
    is_admin = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'real_name'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def activity_periods(self):
        return self.activity_set.all()

    objects = MyActivityManager()

# Child Model for User to add Activity of each user


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,null=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
