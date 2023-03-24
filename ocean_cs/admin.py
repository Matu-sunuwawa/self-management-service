from django.contrib import admin
from .models import Savingacc, Creditacc, SavingDetail, CreditDetail
# Register your models here.

admin.site.register(Savingacc)
admin.site.register(Creditacc)
admin.site.register(SavingDetail)
admin.site.register(CreditDetail)