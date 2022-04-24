from rest_framework import serializers
from .models import SalesProspectProfile

class SalesProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesProspectProfile
        fields = '__all__'


    def validate(self, attrs):
        full_name = attrs.get('full_name')

        if full_name is None:
            attrs['full_name'] = attrs['fb_user']
        return attrs
        
    def create(self, validated_data):
        prospect = SalesProspectProfile.objects.create(**validated_data)
        return prospect