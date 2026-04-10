from django.db import models

class Enclosures(models.Model):
    description=models.CharField(max_length=255)
    size=models.IntegerField()
    
    def __str__(self):
        return self.description


class Animais(models.Model):
    name=models.CharField(max_length=260)
    species=models.CharField(max_length=260)
    age=models.IntegerField()
    health=models.CharField(max_length=260)
    enclosure=models.ForeignKey(Enclosures,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
