from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Savingacc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # invo_id = models.ForeignKey(SavingDetail, on_delete=models.CASCADE)
    camount = models.IntegerField()

class Creditacc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    camount = models.IntegerField()

class SavingDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # inv_id = models.IntegerField()
    deposite = models.IntegerField()
    withdraw = models.IntegerField()

    def __str__(self):
        return str(self.deposite)

class CreditDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    deposite = models.IntegerField()
    withdraw = models.IntegerField()

# class Admin(models.Model):


# class user(models.Model):
    

