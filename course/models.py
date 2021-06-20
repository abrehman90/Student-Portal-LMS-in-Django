from django.db import models
#3rd apps field
from ckeditor.fields import RichTextField
# Create your models here.


class PaidCourse(models.Model):
    course = models.CharField(max_length=100,verbose_name='Course Name')
    desciption = RichTextField(default='open',blank=True,null=True)
    photo = models.ImageField(upload_to='Course/images',verbose_name='Cover Photo')
    video = models.FileField(upload_to='Course/video',verbose_name='Tittle Video')
    price = models.IntegerField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course


Select = (
	('basic', 'Basic'),
	('standard', 'STANDARD'),
	('premium', 'PREMIUM'),
)



class PricePlan(models.Model):
    pakg = models.CharField(choices=Select,default='basic',max_length=8)
    tittle = models.CharField(max_length=100)
    foffere = models.CharField(max_length=50,verbose_name='First Offer',blank=True,null=True)
    soffere = models.CharField(max_length=50,verbose_name='Second Offer',blank=True,null=True)
    toffere = models.CharField(max_length=50,verbose_name='Third Offer',blank=True,null=True)
    fouoffere = models.CharField(max_length=50,verbose_name='Four Offer',blank=True,null=True)
    fivoffere = models.CharField(max_length=50,verbose_name='Five Offer',blank=True,null=True)
    price = models.IntegerField(default=0.0)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle

