from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    shift=models.IntegerField(null=True, help_text='Number between 1 and 25')
    prime_1=models.IntegerField(null=True, help_text='First Favorite Prime')
    prime_2=models.IntegerField(null=True, help_text='Second Favorite Prime')    
    RSA_n=models.IntegerField(null=True, help_text='Modulo n')
    RSA_public_key = models.IntegerField(null=True, help_text='Public Key')
    RSA_private_key= models.IntegerField(null=True, help_text='Private Key')
		
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
	RSA_public_key = models.IntegerField(null=True, help_text='Public Key')
	RSA_private_key= models.IntegerField(null=True, help_text='Private Key')
	RSA_n=models.IntegerField(null=True, help_text='Product of primes')

@receiver(post_save, sender=User)
def update_user_userkeys(sender, instance, created, **kwargs):
    if created:
        UserKeys.objects.create(user=instance)
    instance.profile.save()
    
@receiver(post_save, sender=User)
def save_user_userkeys(sender, instance, **kwargs):
    instance.userkeys.save()