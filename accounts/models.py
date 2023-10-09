from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created and instance is not None:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Enter Email")
        user = self.model(  # 下に書いたユーザークラスを呼び出す
            username=username,
            email=email,
            # それ以外のフィールドはデフォルトで設定される
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    icon = models.ImageField(null=True, upload_to="icon/")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email


class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=300)
    image = models.ImageField(null=True, upload_to="img/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
