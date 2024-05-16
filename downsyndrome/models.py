from django.db import models

# Create your models here.

class Gender(models.Model):
	gender_id = models.BigAutoField(primary_key=True) #gender id BIG INTEGER NOT NULL AUTO INCREMENT PRIMARY KEY
	gender = models.CharField(max_length=55) #gender VARCHAR(55) NOT NULL!
	created_at = models.DateTimeField(auto_now_add=True) #create at TIMESTAMP DEFAULT CURRENT TIMESTAMP
	update_at = models.DateTimeField(auto_now=True)

	class Meta:
	    db_table = 'genders'

class user(models.Model):
	user_id = models.BigAutoField(primary_key=True)
	first_name = models.CharField(max_length=55)
	middle_name = models.CharField(max_length=55, blank=True)
	last_name = models.CharField(max_length=55)
	age = models. IntegerField()
	birth_date = models.DateField()
	gender = models.Foreignkey(Gender, on_delete=models. CASCADE)
	username = models.CharField(max_length=55)
	password = models. CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'users'