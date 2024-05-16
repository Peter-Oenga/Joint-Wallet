# models.py

from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    member_id = models.AutoField(primary_key=True, default=None)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=128)  # Note: Password will be encrypted
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MonthlySavings(models.Model):
    savings_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    savings_amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings_date = models.DateField()


    def __str__(self):
        return f"Savings of {self.member} - Amount: {self.savings_amount}, Date: {self.savings_date}"

class Fines(models.Model):
    fines_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fine_date = models.DateField()

    def __str__(self):
        return f"Fine for {self.member} - Amount: {self.fine_amount}, Date: {self.fine_date}"




class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    TRANSACTION_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    def __str__(self):
        return f"Transaction for {self.member} - Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.transaction_date}"


class Loans(models.Model):
    loan_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_date = models.DateField()

    def __str__(self):
        return f"Loan for {self.member} - Amount: {self.loan_amount}, Interest Rate: {self.interest_rate}%, Date: {self.loan_date}"

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment for Loan ID: {self.loan_id} - Amount: {self.payment_amount}, Date: {self.payment_date}"

