from django.db import models

# Create your models here.
class SearchTerm(models.Model):
    q= models.CharField(max_length = 50)
    search_date = models.DateTimeField(auto_now_add=True) 
    ip_address = models.GenericIPAddressField() 
    
    def __unicode__(self): 
        return self.q