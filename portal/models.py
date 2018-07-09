from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import datetime

# Create your models here.
class Slot(models.Model):
	start_date = models.DateField(default=timezone.now, null=True)
	end_date = models.DateField(default=timezone.now, null=True)
	duration = models.IntegerField(default=7,null=True)
	max_strength = models.IntegerField(default=10,null=True)
	present_strength = models.IntegerField(default=0,null=True)
	is_filled = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('portal:all-slots')

	def __str__(self):
		return str(self.start_date) + " - " + str(self.end_date) + " :: " + str(self.present_strength) + " filled"

class Application(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	application_no = models.CharField(max_length=8, default='00XX0000')
	applicant_name = models.CharField(max_length=250, default='')
	GENDER_CHOICES = (
		('M','Male'),
		('F','Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	caste = models.CharField(max_length=100, default='')
	residence_address = models.TextField(default='')
	college_name = models.CharField(max_length=500, default='')
	college_address = models.TextField(default='')
	mobile_no = models.CharField(max_length=10,default='')
	date_of_birth = models.DateField(default=timezone.now)
	email = models.EmailField(null=True)
	applicant_photo = models.FileField(null=True, help_text="upload jpg, jpeg, png files only", validators=[FileExtensionValidator(['jpg','png','jpeg'])])
	noc = models.FileField(null=True,help_text="upload pdf,jpg,jpeg,png files only with size less than 2mb")
	caste_certificate = models.FileField(null=True,help_text="upload pdf,jpg,jpeg,png files only with size less than 2mb")
	internship_type = models.CharField(max_length=50, default="Training")
	duration = models.IntegerField(default=7)
	slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True)
	course = models.CharField(max_length=250,default='')
	year_of_study = models.CharField(max_length=10, default='Third')
	department = models.CharField(max_length=250, default='')
	is_application_filled = models.BooleanField(default=False)
	verified = models.BooleanField(default=False)
	remarks = models.TextField(null=True)

	def get_absolute_url(self):
		return reverse('portal:application-filled')

	def __str__(self):
		return self.application_no

class Fee(models.Model):
	application = models.OneToOneField(Application, on_delete=models.CASCADE)
	fee_receipt = models.FileField(null=True,help_text="upload pdf,jpg,jpeg,png files only with size less than 2mb")
	FEE_CHOICES = (
		('O', 'Online'),
		('C', 'Challan'),
	)
	fee_type = models.CharField(max_length=1, choices=FEE_CHOICES, default='O')
	transaction_no = models.CharField(max_length=20,default='')
	fees = models.FloatField(default=200.0)
	paid_on = models.DateTimeField(default=timezone.now,help_text="enter only date in yyyy/mm/dd format")
	is_fees_paid = models.BooleanField(default=False)
	verified = models.BooleanField(default=False)
	remarks = models.TextField(null=True)

	def get_absolute_url(self):
		return reverse('portal:applications')

	def __str__(self):
		return str(self.transaction_no)
