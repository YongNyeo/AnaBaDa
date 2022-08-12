from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 user 생성

    def create_user(self, account_id, email, nickname, name, phone_number, password=None):

        if not account_id:
            raise ValueError('must have user ID')
        user = self.model(
            account_id=account_id,
            email=self.normalize_email(email),
            nickname=nickname,
            name=name,
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, account_id,email, nickname, name,phone_number, password):
        user = self.create_user(
            account_id=account_id,
            email= email,
            password=password,
            nickname=nickname,
            name=name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    account_id = models.CharField(primary_key=True,max_length=15, null=False, blank=False, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, unique=True)
    name = models.CharField(default='', max_length=100)
    phone_number = models.CharField(max_length=15 )

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()


    USERNAME_FIELD = 'account_id'
    # superuser만들때도 필수로 작성해야하는 field, 일반유저도 o
    REQUIRED_FIELDS = ['email','nickname','name','phone_number']

    def __str__(self):
        return self.account_id

    @property
    def is_staff(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True