from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(blank=False,null=False)
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name