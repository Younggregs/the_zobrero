from rest_framework import serializers
from .models import Account, WhatDoYouDo, WhatCanYouDo, WhatHaveYouDone, Category, Talent, Employee, WhatsNew, Status

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class AddAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname','lastname','email','password']


class ObreroAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname','lastname','email','password']


class WCYDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname','lastname','email','password']


class WHYDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname','lastname','email','password']



class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email','password']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TalentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talent
        fields = ['id','talent']



class EmployeeListSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    talent = serializers.CharField()


class SearchSerializer(serializers.Serializer):
    search_phrase = serializers.CharField()


class ErrorMessageSerializer(serializers.Serializer):
    message = serializers.CharField()


class SuccessCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()


class RecentActivitySerializer(serializers.Serializer):

    employee_id = serializers.IntegerField()


class TopRatedSerializer(serializers.Serializer):

    employee_id = serializers.IntegerField()



class WhatsNewSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhatsNew
        fields = '__all__'



class ChatClientSerializer(serializers.Serializer):

    name = serializers.CharField()
    client_id = serializers.IntegerField()
    chat_id = serializers.IntegerField()




class MessageSerializer(serializers.Serializer):

    msg = serializers.CharField()
    from_or_to = serializers.BooleanField()




class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'