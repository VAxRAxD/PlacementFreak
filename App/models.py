from django.db import models
from django.contrib.auth.models import AbstractUser
from PlacementFreak.storage import UserMediaStorage

class User(AbstractUser):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    profile=models.ImageField(null=True,blank=True,storage=UserMediaStorage())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
    
class Batch(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return str(self.name-1)+"-"+str(self.name)
    
class Company(models.Model):
    name = models.CharField(max_length=200)
    batches=models.ManyToManyField(Batch)

    def __str__(self):
        return self.name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    verified=models.CharField(max_length=10,default="No",choices=(
        ('Yes','Yes'),('No','No')))
    selected = models.CharField(max_length=100, choices=(
        ('Yes', 'Yes'), ('No', 'No'), ('Response Awaited', 'Response Awaited')))
    difficulty = models.CharField(max_length=100, choices=(
        ('Easy', 'Easy'), ("Medium", 'Medium'), ('Hard', 'Hard')))
    package = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.user.username+" "+self.company.name+" "+str(self.batch.name)