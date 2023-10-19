
from .models import TestKit, User
from rest_framework import serializers

class TestKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestKit
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    test_kit_id = TestKitSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'test_kit_id',)

class ProfileSerializer(serializers.ModelSerializer):
    test_kit = TestKitSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'test_kit_id',)