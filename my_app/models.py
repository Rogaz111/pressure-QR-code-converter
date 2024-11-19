from django.db import models


#Employee Model
class Employee(models.Model):
    employee_name = models.CharField(max_length=225)
    employee_id = models.CharField(max_length=15)


#Pressure Reading Model
class PressureReading(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE)
    sample_number = models.CharField(max_length=15)
    fruit_type = models.CharField(max_length=10, choices=[('apple', 'Apple'), ('pear', 'Pear')])
    reading_1 = models.DecimalField(max_digits=5,decimal_places=2)
    reading_2 = models.DecimalField(max_digits=5,decimal_places=2)
    capture_date = models.DateTimeField()
    sample_status = models.CharField(max_length=1,choices=[('I', 'I'), ('R', 'R'), ('S', 'S'), ('Z', 'Z')])
    capture_station = models.CharField(max_length=225)