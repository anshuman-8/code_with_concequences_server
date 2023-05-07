from django.contrib.auth.models import User, Group
from .models import Organisation, Payment, Social
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ['id','name', 'location', 'about', 'image', 'funds_required', 'funds_raised', 'phone', 'email']

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','donor_name','donor_email', 'organisation', 'mode','message', 'date', 'payment_id']

class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = ['phone', 'email']