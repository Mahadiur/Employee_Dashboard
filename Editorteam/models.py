from django.db import models

# Create your models here.
class EditorTeam(models.Model):
    Full_Name = models.CharField(max_length=50, help_text='Your Full Name ..', blank=False)
    Designation = models.CharField(max_length=50, help_text='Your Current Job Position ..')
    Email = models.CharField(max_length=50, unique=True, help_text='Enter Unique E-mail Address ..', blank=False)
    Photo = models.ImageField(upload_to='Images', help_text='Your Photo ..')
    Phone_Number = models.CharField (max_length=11, unique=True,help_text='Enter Phone Number ..', blank=False)
    Salary = models.DecimalField(max_digits=50, decimal_places=2, help_text='Your Current Salary ..')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Name' + ' ' + self.Full_Name