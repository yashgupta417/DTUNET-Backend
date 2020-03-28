from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        #Don't forget to submit it in apps.py file
        instance.is_active=True
        instance.set_password(instance.password)
        instance.save()
        Token.objects.create(user=instance)
