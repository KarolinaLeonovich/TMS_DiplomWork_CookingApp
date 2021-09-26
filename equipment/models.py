from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.PositiveSmallIntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=50)
    serial = models.PositiveSmallIntegerField()
    in_use = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class PositionQuantity(models.Model):
    position_name = models.OneToOneField(Position, on_delete=models.CASCADE, primary_key=True,)
    position_quantity = models.PositiveSmallIntegerField()





