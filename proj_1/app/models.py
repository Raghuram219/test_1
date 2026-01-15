from django.db import models

class TestModel(models.Model):
    var_1 = models.IntegerField(default=0,null=True,blank=True)
    var_2 = models.CharField(max_length=20,default=0,null=True,blank=True)
    def __str__(self):
        return str(self.id)
