from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
import datetime
from django.db.models.signals import(
    pre_save,
    post_save,
    pre_delete,
    post_delete
)

User = settings.AUTH_USER_MODEL

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, *args, **kwargs):
    # instance.save()
    print(instance.username,  instance.id)

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, *args, **kwargs):
    if created:
        print("Send email to ", instance.username)

        # Triggers a pre_save
        instance.save()
    else:
        print(instance.username, "was just saved")


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active_now = models.BooleanField(default=True)

@receiver(pre_save, sender=BlogPost)
def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.slugify(instance.title)
    if instance.slug and instance.notify_users:
        print("notify_users")
    instance.notify_users = False
    instance.notify_users_timestamp = timezone.now()

@receiver(post_save, sender=BlogPost)
def blog_post_save(sender, instance, created, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.slugify(instance.title)
        instance.save()

@receiver(pre_delete, sender=BlogPost)
def blog_pre_delete(sender, instance, *args, **kwargs):
    print(f"{instance.id} has been removed")


@receiver(post_delete, sender=BlogPost)
def blog_post_delete(sender, instance, created, *args, **kwargs):
    print(f"{instance.id} has been removed")
    

class MonthlySaving(models.Model):
    savings_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    savings_amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings_date = models.DateField()

    def __str__(self):
        return f"Savings of {self.member} - Amount: {self.savings_amount}, Date: {self.savings_date}"

class Fine(models.Model):
    fines_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fine_date = models.DateField()

    def __str__(self):
        return f"Fine for {self.member} - Amount: {self.fine_amount}, Date: {self.fine_date}"

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    TRANSACTION_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    def __str__(self):
        return f"Transaction for {self.member} - Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.transaction_date}"

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f"Loan for {self.member} - Amount: {self.loan_amount}, Interest Rate: {self.interest_rate}%, Date: {self.loan_date}"

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment for Loan ID: {self.loan_id} - Amount: {self.payment_amount}, Date: {self.payment_date}"
