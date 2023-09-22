from django.db import models

# Create your models here. (This is for databases)

class todo(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class item(models.Model):
    todolist = models.ForeignKey(todo, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text