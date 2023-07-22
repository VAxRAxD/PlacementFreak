from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    profile=models.ImageField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
    
class Batch(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=200)
    batches=models.ManyToManyField(Batch)

    def __str__(self):
        return self.name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    message = models.TextField()
    selected = models.CharField(max_length=100, choices=(
        ('Yes', 'Yes'), ('No', 'No'), ('Response Awaited', 'Response Awaited')))
    difficulty = models.CharField(max_length=100, choices=(
        ('Easy', 'Easy'), ("Medium", 'Medium'), ('Hard', 'Hard')))
    package = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.user.username+" "+self.company.name+" "+self.batch.name
    
class Referals(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company=models.CharField(max_length=100, null=True)
    role=models.CharField(max_length=50, null=True)
    description=models.TextField()
    
    def __str__(self):
        return self.user.username+"'s referral for "+self.company.name