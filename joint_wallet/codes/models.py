from django.db import models
from application1.models import CustomUser
import random
# Create your models here.

class Code(models.Model):
    number = models.CharField(max_length=12, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
    
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []
        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)
            code_string = "".join(str(item) for item in(code_items))
            self.number = code_string

        super.save(*args, **kwargs)
