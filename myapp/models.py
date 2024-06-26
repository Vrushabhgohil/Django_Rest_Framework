from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name