from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=False,
            is_active=True,
            is_superuser=False,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            is_staff=True,
            is_active=True,
            is_superuser=True,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True)
    is_doctor = models.BooleanField(default=False, null=True)
    is_patient = models.BooleanField(default=False, null=True)
    address = models.CharField(max_length=200, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def doc_email(self):
        return self.email


class ExtendedDoctorsDetail(models.Model):
    specializations = (('Dermatologists', 'Dermatologists'),
                       ('Family Physicians', 'Family Physicians'),
                       ('Gastroenterologists', 'Gastroenterologists'))
    doctor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_detail', primary_key=True)
    specialization = models.CharField(max_length=50, choices=specializations, null=True)
    open_time = models.IntegerField(default=1, validators=[MaxValueValidator(24), MinValueValidator(1)], null=True)
    close_time = models.IntegerField(default=2, validators=[MaxValueValidator(24), MinValueValidator(1)], null=True)
    is_verified = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.doctor.email


class ExtendedPatientsDetail(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_detail', primary_key=True)
    age = models.IntegerField(null=True, default=0, validators=[MaxValueValidator(120), MinValueValidator(1)])

    def __str__(self):
        return self.patient.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_doctor:
        ExtendedDoctorsDetail.objects.create(doctor=instance)
    elif created and instance.is_patient:
        ExtendedPatientsDetail.objects.create(patient=instance)


'''@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    if instance.is_doctor:
        instance.doctor_detail.save()
        print('user saved with', instance.doctor_detail.specialization)
    elif instance.is_patient:
        instance.patient_detail.save()
'''
