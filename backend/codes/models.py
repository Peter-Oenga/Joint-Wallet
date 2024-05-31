# from django.db import models
# from django.conf import settings
# from django.utils.text import slugify


# from django.dispatch import receiver
# from django.db.models.signals import(
#     post_save
# )

# User = settings.AUTH_USER_MODEL

# @receiver(post_save, sender=User)
# def user_created_handler(*args, **kwargs):
#     print(args, kwargs)

# #post_save.connect(user_created_handler, sender=User)