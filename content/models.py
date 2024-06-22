from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='project_images/')
    repository = models.URLField()
    technologies = models.ManyToManyField(Technology)
    
    def __str__(self):
        return self.name
