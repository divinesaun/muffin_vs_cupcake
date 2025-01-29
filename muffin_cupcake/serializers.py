from rest_framework import serializers

class Data(serializers.Serializer):
    Flour = serializers.IntegerField()
    Milk = serializers.IntegerField()
    Sugar = serializers.IntegerField()
    Butter = serializers.IntegerField()
    Egg = serializers.IntegerField()
    Baking_Powder = serializers.IntegerField()
    Vanilla = serializers.IntegerField()
    Salt = serializers.IntegerField()