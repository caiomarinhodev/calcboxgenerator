from rest_framework import viewsets

from . import (
    serializers,
    models
)


class DrawViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.DrawSerializer
    queryset = models.Draw.objects.all()

class BoxViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.BoxSerializer
    queryset = models.Box.objects.all()

