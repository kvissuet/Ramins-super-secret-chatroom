from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    shift=models.IntegerField(null=True, help_text='Number between 1 and 25')
    prime_1=models.IntegerField(null=True, help_text='First Favorite Prime')
    prime_2=models.IntegerField(null=True, help_text='Second Favorite Prime')
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class UserKeys(models.Model):
	"""Public Keys given to all users"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	RSA_public_key = models.IntegerField(null=True, help_text='First Favorite Prime')
	RSA_private_key= models.IntegerField(null=True, help_text='Second Favorite Prime')
	RSA_n=models.IntegerField(null=True, help_text='First Favorite Prime')
	
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.RSA_public_key