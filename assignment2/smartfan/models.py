from django.db import models

# Create your models here.

class fanStatus(models.Model):
    id = models.IntegerField(primary_key= True)
    Temperature = models.IntegerField()
    # On / Off
    Status = models.CharField(max_length=5) 
    Date = models.DateTimeField()
    # Auto / Manual
    Mode = models.CharField(max_length=10)

# method to return all the fields

def __str__(self):
    return self.id + self.Temperature + self.Status + self.Date + self.Mode
