from django.db import models


# Create your models here.

class TrueCallerData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=50, null=True)
    create_time = models.DateTimeField(null=True)

    def __str__(self):
        return '%s | %s | %s' % (self.id, self.name, self.create_time)

class GameData(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TrueCallerData)
    car_type = models.CharField(max_length=100, null=True)
    nil_depreciation_cover=models.BooleanField(default=True)
    idv=models.CharField(max_length=100, null=True)
    personal_accident_cover=models.BooleanField(default=True)
    member_of_automobile_association=models.BooleanField(default=True)
    protection_for_accessories=models.BooleanField(default=False)
    voluntary_deductible=models.CharField(max_length=20)
    create_time = models.DateTimeField(null=True)
    PA_cover_for_un_named_passengers=models.BooleanField(default=False)



