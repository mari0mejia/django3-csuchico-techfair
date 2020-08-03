from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Company(models.Model):

    YEAR_LEVEL = (
        (1,'Freshman'),
        (2,'Sophomore'),
        (3,'Junior'),
        (4,'Senior'),
        (5,'Graduate'),
        (6,'Working Experience'),
    
    )
    MAJOR_TYPES = (
        (1,'Computer Animation & Game Development'),
        (2,'Civil Engineering'),
        (3,'Computer Engineering'),
        (4,'Computer Information Systems'),
        (5,'Computer Science'),
        (6,'Construction Industry Management'),
        (7,'Concrete Industry Management'),
        (8,'Contstruction Management'),
        (9,'Electrical Engineering'),
        (10,'Mechanical Engineering'),
        (11,'Mechatronic Engineering'),
        (12,'Sustainable Manufacturing'),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    logo = models.ImageField(upload_to = 'tech_fair/images/') 
    url = models.URLField()
    email = models.EmailField(max_length = 254)
    business_email = models.EmailField(max_length=254)
    education_level = MultiSelectField(choices = YEAR_LEVEL ,max_length=6)
    major = MultiSelectField(choices = MAJOR_TYPES,max_length =12)

    def __str__(self):
        return self.name
