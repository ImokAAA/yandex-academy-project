from django.db import models

class CourierRegion(models.Model):
    region          = models.IntegerField(primary_key = True)


class Courier(models.Model):
    courier_id      = models.IntegerField(primary_key=True)
    class CourierTypes(models.TextChoices):
        FOOT = 'f'
        BIKE = 'b'
        CAR = 'c'

    courier_type    = models.CharField(max_length=1, choices=CourierTypes.choices)
    regions         = models.ManyToManyField(CourierRegion)
    #workinghour_set can be used
    rating          = models.FloatField(null = True, blank = True)
    earnings        = models.FloatField(null = True, blank = True)


class WorkingHour(models.Model):
    courier_id      = models.ForeignKey(Courier, on_delete=models.CASCADE) 
    start_time      = models.TimeField()
    end_time        = models.TimeField()


