from django.db import models

class Diabet(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI= models.FloatField()
    DiabetesPedigreeFunction= models.FloatField()
    Age = models.IntegerField()
    Outcome = models.BooleanField()
    
class DiabetesFromCsv(models.Model):
    csv_file = models.FileField(upload_to='uploads/')