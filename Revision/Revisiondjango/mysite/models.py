from django.db import models


'''
Reason:
Model banate hai taaki Django database me table create kare aur hum usme data store kar sake.
'''


#💫 Project 1 Employee.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    




#💫 Project 2

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Photo {self.pk}"











