from rest_framework import serializers
from .models import CustomUser
from .models import MonthlySaving, Fine


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'address']

class MonthlySavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlySaving
        fields = '__all__'

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'