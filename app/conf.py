#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.utils.translation import ugettext_lazy as _
from django.conf import LazySettings

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default


# Items by page on paginator views
ITEMS_BY_PAGE = 10

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

API_SUFFIX = "_api"
style = "base_django/flexbox"


# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

CONFIGURING_APPLICATION = _("Configuring application {}")
CREATING_PERMISSION_WITH_NAME = _("Creating Permission with name {}")
CREATING_GROUP_WITH_NAME = _("Creating Group with name {}")


DRAW_PREFIX = "DRAW"

DRAW_VERBOSE_NAME = _("Draw")
DRAW_VERBOSE_NAME_PLURAL = _("Draw")

DRAW_LIST_URL_NAME = DRAW_PREFIX + LIST_SUFFIX
DRAW_CREATE_URL_NAME = DRAW_PREFIX + CREATE_SUFFIX
DRAW_DETAIL_URL_NAME = DRAW_PREFIX + DETAIL_SUFFIX
DRAW_UPDATE_URL_NAME = DRAW_PREFIX + UPDATE_SUFFIX
DRAW_DELETE_URL_NAME = DRAW_PREFIX + DELETE_SUFFIX


BOX_PREFIX = "BOX"

BOX_VERBOSE_NAME = _("Box")
BOX_VERBOSE_NAME_PLURAL = _("Box")

BOX_LIST_URL_NAME = BOX_PREFIX + LIST_SUFFIX
BOX_CREATE_URL_NAME = BOX_PREFIX + CREATE_SUFFIX
BOX_DETAIL_URL_NAME = BOX_PREFIX + DETAIL_SUFFIX
BOX_UPDATE_URL_NAME = BOX_PREFIX + UPDATE_SUFFIX
BOX_DELETE_URL_NAME = BOX_PREFIX + DELETE_SUFFIX

