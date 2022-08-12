from account.models import Member
from rest_framework import serializers


class Aserializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Member.objects.create_user(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            name=validated_data['name'],
            password=validated_data['password'],
            account_id=validated_data['account_id'],
            phone_number=validated_data['phone_number']
        )
        return user

    class Meta:
        model = Member
        fields = '__all__'
