from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have a email address')

        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name= models.CharField(_('Primeiro Nome'), max_length=50)
    last_name = models.CharField(_('Ultimo Nome'), max_length=50)
    username  = models.CharField(_('Login'), max_length=50, unique=True)
    email     = models.EmailField(_('E-Mail'), max_length=100, unique=True)
    phone_number  = models.CharField(_('Telefone'), max_length=50)

    # Obrigatorios
    date_joined   = models.DateTimeField(auto_now_add=True)
    last_login    = models.DateTimeField(auto_now_add=True)
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'nome', 'sobrenome')

    class Meta:
        verbose_name = _('Conta')
        verbose_name_plural = _('Contas')

    def __str__(self):
        return f'{self.username} - {self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_model_perm(self, add_label):
        return True
