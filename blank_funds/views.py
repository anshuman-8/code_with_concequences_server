from django.shortcuts import render
from rest_framework import viewsets, response, request
from .models import Organisation, Payment, Social
from .serializers import OrganisationSerializer, PaymentSerializer, SocialSerializer
from rest_framework.decorators import api_view


class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


@api_view(['GET'])
def getOrganisations(request):
    organisations = Organisation.objects.all()
    serializer = OrganisationSerializer(organisations, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def getOrganisation(request):
    oid = request.GET.get('id')
    organisation = Organisation.objects.get(id=oid)
    serializer = OrganisationSerializer(organisation, many=False)
    return response.Response(serializer.data)

@api_view(['POST'])
def createOrganisation(request):
    serializer = OrganisationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)