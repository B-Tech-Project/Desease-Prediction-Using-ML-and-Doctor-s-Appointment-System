from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import User, ExtendedDoctorsDetail, ExtendedPatientsDetail


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'name', 'address',)


class ExtendedDoctorsDetailForm(ModelForm):
    class Meta:
        model = ExtendedDoctorsDetail
        fields = ('specialization', 'open_time', 'close_time')


class ExtendedPatientsDetailForm(ModelForm):
    class Meta:
        model = ExtendedPatientsDetail
        fields = ('age',)

# to update user profile


class UpdateUserProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'address')


class UpdateDoctorProfile(ModelForm):
    class Meta:
        model = ExtendedDoctorsDetail
        fields = ('specialization', 'open_time', 'close_time')


class UpdatePatientProfile(ModelForm):
    class Meta:
        model = ExtendedPatientsDetail
        fields = ('age',)