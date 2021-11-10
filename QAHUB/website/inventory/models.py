from django.db import models
from django import forms


# Create your models here.


class materialForm(models.Model):

    Name_of_the_Material_per_specification = models.CharField(max_length=100, null=True)
    Site_Material_Code = models.CharField(max_length=100, null=True) 
    Lot_Number = models.CharField(max_length=100, null=True) 
    orderForm = forms.FileField(label='Purchase Order Form:')
    slip = forms.FileField(label='Packing Slip:')
    Purchase_Order = models.CharField(max_length=100, null=True) 
    Material_Identity = models.CharField(max_length=100, null=True)  
    Quantity = models.CharField(max_length=100, null=True) 
    #needs to update with batch record
    Supplier_Name = models.CharField(max_length=100, null=True) 
    Supplier_Lot_Number = models.CharField(max_length=100, null=True) 
    Manufacturer = models.CharField(max_length=100, null=True) 
    Site_Lot_Number = models.CharField(max_length=100, null=True) 
    Receipt_Date = models.CharField(max_length=100, null=True) 
    #GMP format
    Personnel = models.CharField(max_length=100, null=True) 
    Comments = models.CharField(max_length=400, null=True) 
    #<p>Comments:
    #<textarea rows="4" cols="50" name="comment"></textarea></p>
    MSDS = models.CharField(max_length=100, null=True) 

    def __str__(self):
        return self.Name_of_the_Material_per_specification

class inv(models.Model):
    material = models.ForeignKey(materialForm, null=True, on_delete= models.SET_NULL)
    
    def __str__(self):
	    return self.material


