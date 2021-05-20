#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import FieldDoesNotExist
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, DeleteView, UpdateView
)
from django.views.generic.list import ListView


try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy, reverse

from app.models import Draw
from app.forms import DrawForm
from app.mixins import DrawMixin
from app.conf import DRAW_DETAIL_URL_NAME, DRAW_CREATE_URL_NAME, \
DRAW_LIST_URL_NAME, DRAW_UPDATE_URL_NAME, \
DRAW_DELETE_URL_NAME


class List(LoginRequiredMixin, DrawMixin, ListView):
    """
    List all Draws
    """
    login_url = '/admin/login/'
    queryset = Draw.objects.all()
    template_name = 'draw/list.html'
    model = Draw
    context_object_name = 'draws'
    ordering = '-created_at'

    def get_queryset(self):
        return Draw.objects.all()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['detail_url_name'] = DRAW_DETAIL_URL_NAME
        context['delete_url_name'] = DRAW_DELETE_URL_NAME
        if self.request.user.has_perm("app.add_draw"):
            context['create_object_reversed_url'] = reverse_lazy(
                DRAW_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, DrawMixin, PermissionRequiredMixin, CreateView):
    """
    Create a Draw
    """
    login_url = '/admin/login/'
    model = Draw
    permission_required = (
        'app.add_draw'
    )
    form_class = DrawForm
    template_name = 'draw/create.html'
    context_object_name = 'draw'

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(DRAW_LIST_URL_NAME)
        return context

    def get_success_url(self):
        return reverse_lazy(DRAW_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_initial(self):
        data = super(Create, self).get_initial()
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Draw criado com sucesso')
        return super(Create, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Create, self).form_invalid(form)


class Detail(LoginRequiredMixin, DrawMixin, DetailView):
    """
    Detail of a Draw
    """
    login_url = '/admin/login/'
    model = Draw
    template_name = 'draw/detail.html'
    context_object_name = 'draw'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(DRAW_LIST_URL_NAME)
        if self.request.user.has_perm("app.change_draw"):
            context['update_object_reversed_url'] = reverse_lazy(
                DRAW_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("app.delete_draw"):
            context['delete_object_reversed_url'] = reverse_lazy(
                DRAW_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )
        return context


class Update(LoginRequiredMixin, DrawMixin, PermissionRequiredMixin, UpdateView):
    """
    Update a Draw
    """
    login_url = '/admin/login/'
    model = Draw
    template_name = 'draw/update.html'
    context_object_name = 'draw'
    form_class = DrawForm
    permission_required = (
        'app.change_draw'
    )

    def get_initial(self):
        data = super(Update, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy(DRAW_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_context_data(self, **kwargs):
        data = super(Update, self).get_context_data(**kwargs)
        data['list_reversed_url'] = reverse_lazy(DRAW_LIST_URL_NAME)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Draw atualizado com sucesso')
        return super(Update, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Update, self).form_invalid(form)


class Delete(LoginRequiredMixin, DrawMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete a Draw
    """
    login_url = '/admin/login/'
    model = Draw
    permission_required = (
        'app.delete_draw'
    )
    template_name = 'draw/delete.html'
    context_object_name = 'draw'

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(DRAW_LIST_URL_NAME)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(Delete, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Draw removido com sucesso')
        return super(Delete, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(DRAW_LIST_URL_NAME)
