from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Countries(models.Model):
    name       = models.CharField(max_length=15)
    alphacode2 = models.CharField(max_length=2, blank=True, null=True)
    capital    = models.CharField(max_length=15, blank=True, null=True)
    population = models.CharField( max_length=15, blank = True, null = True)
    timezone   = models.CharField( max_length=15, blank = True, null = True)
    flag_url   = models.CharField( max_length=50, blank = True, null = True)
    languages  = models.CharField(max_length=250, blank=True, null=True)
    slug       = models.SlugField(null=False, unique=True)
    neighbouring_countries = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('country_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.alphacode2)
        return super().save(*args, **kwargs)