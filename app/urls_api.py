from rest_framework.routers import DefaultRouter
from app import (
    viewsets
)

api_urlpatterns = []

draw_router = DefaultRouter()

draw_router.register(
    r'^api/draw',
    viewsets.DrawViewSet,
    basename="draw"
)

api_urlpatterns += draw_router.urls
box_router = DefaultRouter()

box_router.register(
    r'^api/box',
    viewsets.BoxViewSet,
    basename="box"
)

api_urlpatterns += box_router.urls
