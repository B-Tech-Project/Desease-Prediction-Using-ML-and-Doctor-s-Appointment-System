

from django.db import models
from users.models import ExtendedDoctorsDetail, ExtendedPatientsDetail
# Create your models here.


class Booking(models.Model):
    patient_email = models.ForeignKey(ExtendedPatientsDetail, on_delete=models.CASCADE, primary_key=False, null=True)
    doctor_email = models.ForeignKey(ExtendedDoctorsDetail, on_delete=models.CASCADE, primary_key=False, null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.patient_email.patient.email