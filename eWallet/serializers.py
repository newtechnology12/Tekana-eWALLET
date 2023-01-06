
from logging import raiseExceptions
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.urls import reverse_lazy
from django.utils.html import format_html
from .models import *


class PaymentMethodSerielizer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"
    

class AccountSerielizer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class BankSerielizer(serializers.ModelSerializer):


    class Meta:
        model = Bank
        fields = '__all__'

class CardTypeSerielizer(serializers.ModelSerializer):

    class Meta:
        model = CardType
        fields = '__all__'

class Transaction_TypeSerielizer(serializers.ModelSerializer):

    class Meta:
        model = Transaction_Type
        fields = '__all__'

class TCategoriesSerielizer(serializers.ModelSerializer):

    class Meta:
        model = TCategories
        fields = '__all__'

   

class CardSerielizer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        # exclude = ['user', 'method_type', 'payment']
        fields = '__all__'
    
    


class TransactionSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class RequestMoneySerielizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('category', 'amount', 'description')


class CompletePaymentSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('payment_method', )

  







