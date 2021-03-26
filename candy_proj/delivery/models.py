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
    #order_set
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



class Order(models.Model):
    order_id        = models.IntegerField(primary_key=True)
    courier_id      = models.ForeignKey(Courier, on_delete=models.CASCADE, null = True, blank = True)
    weight          = models.FloatField(null = True, blank = True)
    region          = models.IntegerField()
    assign_time     = models.TimeField(null = True, blank = True)
    complete_time   = models.TimeField(null = True, blank = True)

    def __str__(self):
        return str(self.order_id)

class DeliveryHour(models.Model):
    order_id        = models.ForeignKey(Order, on_delete=models.CASCADE) 
    start_time      = models.TimeField()
    end_time        = models.TimeField()

    def __str__(self):
        return str(self.start_time) +" - "+ str(self.end_time)


