from django.db import models

class Countries(models.Model):
    name       = models.CharField(max_length=15)
    alphacode2 = models.CharField(max_length=2, blank=True, null=True)
    capital    = models.CharField(max_length=15, blank=True, null=True)
    population = models.CharField( max_length=15, blank = True, null = True)
    timezone   = models.CharField( max_length=2, blank = True, null = True)
    flag_url   = models.CharField( max_length=50, blank = True, null = True)
    languages  = models.CharField(max_length=250, blank=True, null=True)
    neighbouring_countries = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name