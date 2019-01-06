from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

# andika.language.all()         : ManyToMani
# andika.company                : ForeignKey
# apple.programmer_set.all()    : ForeignKey
