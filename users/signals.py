#?user modelinden sinyali yakalamak için import ediyoruz.sinyali bu model gönderecek
from django.contrib.auth.models import User

#? post_save pre_save vb birkaç metot var
from django.db.models.signals import post_save

#! receiver decorator ile sinyali yakalarız.
from django.dispatch import receiver

#? token modeli oluşturacağımız token yeri
from rest_framework.authtoken.models import Token

#? User modelinde post_save olmuşsa yani register olmuşsa bana bir token create at diyoruz burda.

@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    
     #! **kwargs çok önemli bunu yazmaksak çalışmaz arkada tarafta kulladığı argümanları alır.
     
     if created:
        Token.objects.create(user=instance)
        
        # buradaki instance User modelinde create olmuş user oluyor
        # user ise Token modelindeki bir field(onetoonefield olarak ayarlanmış yani bir userın bir tokenı olur)
        # bunun çalışması için apps.py işlem gerekir.
     

