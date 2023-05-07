from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('org/', views.getOrganisation, name='getOrganisation'),
    path('orgs/', views.getOrganisations, name='getOrganisations'),
    path('createOrg/', views.createOrganisation, name='createOrganisation'),
    path('pay/',views.createPayment, name='make Payment'),
    path('orgPayments/',views.getOrgPayments, name='getOrgPayments'),
    path('createUser/',views.createUser, name='createUser')
]