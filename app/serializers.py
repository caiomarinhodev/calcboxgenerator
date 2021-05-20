from rest_framework import serializers


from app.models import Draw
class DrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draw
        fields = '__all__'


from app.models import Box
class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'


