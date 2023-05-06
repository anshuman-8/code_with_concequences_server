from .models import User, Organisation, Payment, Social
from .serializers import OrganisationSerializer, PaymentSerializer, SocialSerializer, UserSerializer
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('org/', views.getOrganisation, name='getOrganisation'),
    path('orgs/', views.getOrganisations, name='getOrganisations'),
    path('createOrg/', views.createOrganisation, name='createOrganisation'),
]