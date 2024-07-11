from django.db import models

class Book(models.Model):
    title_description = models.TextField()
    contributors = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    place_origin = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=100)
    genre = models.TextField(null=True, blank=True) #bucolica, georgica, aeneid, etc.
    call_num = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    image_loc = models.FileField(upload_to="bookcat_images/", null=True, blank=True)
    image_str = models.TextField(null=True, blank=True)
    barcode = models.CharField(max_length=50, null=True, blank=True)
    loc_code = models.CharField(max_length=50, null=True, blank=True)
    BM_cat = models.CharField(max_length=50, null=True, blank=True)
    #MultiValueField for barcode/callnum etc?
    
    #potentialy translated tiitel:
    #set required = false so can have empty slots