from django.db import models

class CourierRegion(models.Model):
    region          = models.IntegerField(primary_key = True)
    
    def __str__(self):
        return str(self.region)

class Courier(models.Model):
    courier_id      = models.IntegerField(primary_key=True)
    courier_type    = models.CharField(max_length=4)
    regions         = models.ManyToManyField(CourierRegion)
    #workinghour_set can be used
    rating          = models.FloatField(null = True, blank = True)
    earnings        = models.FloatField(null = True, blank = True)
    
    def __str__(self):
        return str(self.courier_id)

class WorkingHour(models.Model):
    courier_id      = models.ForeignKey(Courier, on_delete=models.CASCADE) 
    start_time      = models.TimeField()
    end_time        = models.TimeField()

    def __str__(self):
        return str(self.start_time) +" - "+ str(self.end_time)

