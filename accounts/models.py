from sre_constants import CATEGORY
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings

class Investor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="user_icon.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    CATEGORY = (
            ('Idea-phase', 'Idea-phase'),
            ('Semi-completed', 'Semi-completed'),
            ('Fully-completed', 'Fully-completed'),

            )
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    descripton = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.name)

class Investment(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Verified', 'Verified'),
            ('Matured', 'Matured'),
            )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    investor = models.ForeignKey(Investor, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(100),
                                       MaxValueValidator(900000)], null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(default='Pending', max_length=200, null=True, choices=STATUS)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.amount) 

