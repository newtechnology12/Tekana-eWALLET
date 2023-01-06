from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class PaymentMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    method_type = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, related_name='payment_user', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.method_id)


class Account(models.Model):
    payment = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.00)

    def __str__(self):
        return 'Account: %s' % self.payment.user.username

    def get_update_url(self):
        return reverse('account_transfer', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # ensure that the database only stores 2 decimal places
        self.balance = round(self.balance, 2)
        super(Account, self).save(*args, **kwargs)


class Bank(models.Model):
    payment = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)
    owner_first_name = models.CharField(max_length=255, default=None)
    owner_last_name = models.CharField(max_length=255, default=None)
    routing_number = models.CharField(max_length=9, default=None)
    account_number = models.CharField(max_length=10, default=None)

    def __str__(self):
        return 'Bank: ****%s' % self.account_number[5:]

    def get_absolute_url(self):
        return reverse('bank_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('bank_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('bank_delete', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ('routing_number', 'account_number')


# Card_Type = (
#     ('Credit', 'Credit Card'),
#     ('Debit', 'Debit Card'),
# )

class CardType(models.Model):
    cardName = models.CharField(max_length=40, blank=True, null = True)


    def __str__(self) -> str:
        return self.cardName

class Card(models.Model):
    payment = models.OneToOneField(PaymentMethod, on_delete=models.DO_NOTHING)
    card_type = models.ForeignKey(CardType,on_delete=models.PROTECT, max_length=45)
    card_number = models.CharField(max_length=16, default=None)
    owner_first_name = models.CharField(max_length=45)
    owner_last_name = models.CharField(max_length=45)
    security_code = models.CharField(max_length=3, default=None)
    expiration_date = models.DateField(default=None)

    def get_absolute_url(self):
        return reverse('card_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('card_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('card_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s Card: ************%s' % (self.card_type, self.card_number[12:])

    class Meta:
        unique_together = ('card_type', 'owner_first_name', 'owner_last_name',
                           'card_number', 'security_code', 'expiration_date')
        ordering = ['card_type', 'card_number']


# Transaction_Type = (
#     ('send', 'Send'),
#     ('request', 'Request'),
#     ('transfer', 'Transfer'),
# )

class Transaction_Type(models.Model):
    transactionName = models.CharField(max_length=20,blank=True, null= True)

    def __str__(self) -> str:
        return self.transactionName

# Categories = (
#     ('Bank', 'Bank Transfer'),
#     ('Utilities', 'Bills & Utilities'),
#     ('Transportation', 'Auto & Transport'),
#     ('Groceries', 'Groceries'),
#     ('Food', 'Food'),
#     ('Shopping', 'Shopping'),
#     ('Health', 'Healthcare'),
#     ('Education', 'Education'),
#     ('Travel', 'Travel'),
#     ('Housing', 'Housing'),
#     ('Entertainment', 'Entertainment'),
#     ('Others', 'Others'),
# )

class TCategories(models.Model):
    transactionCatrgory = models.CharField(max_length=20,blank=True, null= True)

    def __str__(self) -> str:
        return self.transactionCatrgory

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.ForeignKey(Transaction_Type, on_delete=models.PROTECT,blank=True,null=True, max_length=45)
    category = models.ForeignKey(TCategories,on_delete=models.PROTECT, max_length=45)
    amount = models.FloatField(default=0.00)
    description = models.CharField(max_length=200, default=False)
    create_date = models.DateTimeField(default=now, editable=False)
    is_complete = models.BooleanField(default=False)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.PROTECT, default='')
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.PROTECT, default='')
    payment_method = models.ForeignKey(PaymentMethod, related_name='payment_method',
                                       on_delete=models.PROTECT, default='', null=True)

    def get_absolute_url(self):
        return reverse('staff_tran_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('staff_tran_delete', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # ensure that the database only stores 2 decimal places
        self.amount = round(self.amount, 2)
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.transaction_id)

    class Meta:
        ordering = ['category']