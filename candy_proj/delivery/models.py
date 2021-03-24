from django.db import models
import json

class Courier(models.Model):
    """ Stores data about couriers """
    courier_id      = models.AutoField(primary_key=True)
    courier_type    = models.CharField(max_length=255)
    regions         = models.CharField(max_length=255) #used with methods
    working_hours   = models.CharField(max_length=255) #used with methods

    # used for regions
    def set_regions(self, regions_list):
        "Converts list to string to store in database"
        self.regions = json.dumps(regions_list)

    def get_regions(self):
        "Converts string to list to get from database"
        return json.loads(self.regions) 
    
    #used for working_hours
    def set_working_hours(self, working_hours_list):
        "Converts list to string to store in database"
        self.working_hours = json.dumps(working_hours_list)

    def get_working_hours(self):
        "Converts string to list to get from database"
        return json.loads(self.working_hours)


 


