from django.urls import path

from app import conf

from app.urls_api import api_urlpatterns

urlpatterns = []

from app.views import draw
urlpatterns += [
    # draw
    path(
        'draw/',
        draw.List.as_view(),
        name=conf.DRAW_LIST_URL_NAME
    ),
    path(
        'draw/create/',
        draw.Create.as_view(),
        name=conf.DRAW_CREATE_URL_NAME
    ),
    path(
        'draw/<int:pk>/',
        draw.Detail.as_view(),
        name=conf.DRAW_DETAIL_URL_NAME
    ),
    path(
        'draw/<int:pk>/update/',
        draw.Update.as_view(),
        name=conf.DRAW_UPDATE_URL_NAME
    ),
    path(
        'draw/<int:pk>/delete/',
        draw.Delete.as_view(),
        name=conf.DRAW_DELETE_URL_NAME
    ),
]

from app.views import box
urlpatterns += [
    # box
    path(
        '',
        box.List.as_view(),
        name=conf.BOX_LIST_URL_NAME
    ),
    path(
        'box/create/',
        box.Create.as_view(),
        name=conf.BOX_CREATE_URL_NAME
    ),
    path(
        'box/<int:pk>/',
        box.Detail.as_view(),
        name=conf.BOX_DETAIL_URL_NAME
    ),
    path(
        'box/<int:pk>/update/',
        box.Update.as_view(),
        name=conf.BOX_UPDATE_URL_NAME
    ),
    path(
        'box/<int:pk>/delete/',
        box.Delete.as_view(),
        name=conf.BOX_DELETE_URL_NAME
    ),
]

urlpatterns += api_urlpatterns
