from django.db import models


#created model called djangoClasses and defined its attributes
class djangoClasses(models.Model):
    title = models.CharField(max_length=60,default="")
    courseNumber = models.IntegerField(default="",unique=True)
    instructorName = models.TextField(max_length=300, default="", blank=True)
    duration = models.DecimalField(default=00.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

#created 3 new instances of djangoClasses model 
classOne = djangoClasses(title='Overview', courseNumber=1,instructorName='',duration=8.00)
classTwo = djangoClasses(title='Requests and Responses', courseNumber=2,instructorName='',duration=16.00)
classThree = djangoClasses(title='Models', courseNumber=3,instructorName='',duration=24.00)
classOne.save()
classTwo.save()
classThree.save()