from django.urls import  path,include
from eWallet import views
from django.contrib.auth import views as auth_views
from .views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny], 
)



urlpatterns = [
    
    path('PaymentMethod', PaymentMethodPIView.as_view(), name='PaymentMethod'),
    path('PaymentMethod/<int:pk>/', DetailcPaymentMethodAPIView.as_view(), name='categorybyid'),
    
    path('Account', AccountAPIView.as_view(), name='Account'),
    path('AccountDetail/<int:pk>/', AccountDetailPIView.as_view(), name='Product'), 
    path('BankPIView', BankPIView.as_view(), name='Account'),
    path('DetailBank/<int:pk>/', DetailBankAPIView.as_view(), name='DetailSale'),

    path('CardType', CardTypePIView.as_view(), name='Account'),
    path('CardType/<int:pk>/', DetailCardTypeAPIView.as_view(), name='Product'), 
    path('Card', CardPIView.as_view(), name='Account'),
    path('Card/<int:pk>/', DetailCardAPIView.as_view(), name='DetailSale'),

    path('Transaction_Type', Transaction_TypeAPIView.as_view(), name='Account'),
    path('Transaction_Type/<int:pk>/', DetailTransaction_TypeAPIView.as_view(), name='Product'), 
    path('TCategories',TCategoriesPIView.as_view(), name='Account'),
    path('TCategories/<int:pk>/', DetailCardAPIView.as_view(), name='DetailSale'),

    path('Transaction', TransactionAPIView.as_view(), name='Account'),
    path('Transaction/<int:pk>/', DetailTransactionAPIView.as_view(), name='Product'), 

    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   
]
