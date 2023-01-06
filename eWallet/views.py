from django.shortcuts import render, redirect
from eWallet.serializers import *
from eWallet.models import *
from django.contrib.auth.decorators import login_required
from eWallet import *

from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from . models import *



# Create your views here.


# all api of my Project

class PaymentMethodPIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerielizer

class DetailcPaymentMethodAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerielizer

class AccountAPIView(generics.ListCreateAPIView):
    # permission_classes = permissions.IsAuthenticatedOrReadOnly
    queryset = Account.objects.all()
    serializer_class = AccountSerielizer
    
class AccountDetailPIView(generics.RetrieveDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser)
    queryset = Account.objects.all()
    serializer_class = AccountSerielizer

class BankPIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = Bank.objects.all()
    serializer_class = BankSerielizer

class DetailBankAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes= (permissions.BasePermission)
    queryset = Bank.objects.all()
    serializer_class = BankSerielizer

class CardTypePIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerielizer

class DetailCardTypeAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes= (permissions.BasePermission)
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerielizer

class CardPIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = Card.objects.all()
    serializer_class = CardSerielizer

class DetailCardAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes= (permissions.BasePermission)
    queryset = Card.objects.all()
    serializer_class = CardSerielizer

class Transaction_TypeAPIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = Transaction_Type.objects.all()
    serializer_class = Transaction_TypeSerielizer

class DetailTransaction_TypeAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes= (permissions.BasePermission)
    queryset = Transaction_Type.objects.all()
    serializer_class = Transaction_TypeSerielizer

class TCategoriesPIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = TCategories.objects.all()
    serializer_class = TCategoriesSerielizer

class DetailTCategoriesAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes= (permissions.BasePermission)
    queryset = TCategories.objects.all()
    serializer_class = TCategoriesSerielizer

class TransactionAPIView(generics.ListCreateAPIView):
    # permission_classes =(permissions.AllowAny)
    queryset = Transaction.objects.all()
    serializer_class = Transaction_TypeSerielizer

class DetailTransactionAPIView(generics.RetrieveDestroyAPIView):
    # permission_classes= (permissions.BasePermission)
    queryset = Transaction.objects.all()
    serializer_class = Transaction_TypeSerielizer