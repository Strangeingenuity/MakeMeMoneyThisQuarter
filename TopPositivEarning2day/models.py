from django.db import models
from decimal import Decimal

class StockCode(models.Model):
    StockCode = models.CharField(max_length=30)
    CompanyName = models.CharField(max_length=100)
    Industry = models.CharField(max_length=30)

    def __str__(self):
        return self.StockCode

class StockEarnings(models.Model):

    StockCode = models.ForeignKey(StockCode, on_delete=models.CASCADE)
    ProjectedEarning = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    LastQuarterEarning = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    LastYearEarning = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    BeatorMissThisQuater = models.BooleanField()
    PositivOrNagetiv = models.BooleanField()
    EntryName = models.CharField(max_length=30,default='Test')

    def __str__(self):
        return self.EntryName

