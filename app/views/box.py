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

from app.models import Box
from app.forms import BoxForm
from app.mixins import BoxMixin
from app.conf import BOX_DETAIL_URL_NAME, BOX_CREATE_URL_NAME, \
BOX_LIST_URL_NAME, BOX_UPDATE_URL_NAME, \
BOX_DELETE_URL_NAME


class List(LoginRequiredMixin, BoxMixin, ListView):
    """
    List all Boxs
    """
    login_url = '/admin/login/'
    queryset = Box.objects.all()
    template_name = 'box/list.html'
    model = Box
    context_object_name = 'boxs'
    ordering = '-created_at'

    def get_queryset(self):
        return Box.objects.all()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['detail_url_name'] = BOX_DETAIL_URL_NAME
        context['delete_url_name'] = BOX_DELETE_URL_NAME
        if self.request.user.has_perm("app.add_box"):
            context['create_object_reversed_url'] = reverse_lazy(
                BOX_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, BoxMixin, PermissionRequiredMixin, CreateView):
    """
    Create a Box
    """
    login_url = '/admin/login/'
    model = Box
    permission_required = (
        'app.add_box'
    )
    form_class = BoxForm
    template_name = 'box/create.html'
    context_object_name = 'box'

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(BOX_LIST_URL_NAME)
        return context

    def get_success_url(self):
        return reverse_lazy(BOX_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_initial(self):
        data = super(Create, self).get_initial()
        return data

    def form_valid(self, form):
        self.object = form.save()
        self.object.save(first_create=True)
        messages.success(self.request, 'Box criado com sucesso')
        return super(Create, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Create, self).form_invalid(form)


class Detail(LoginRequiredMixin, BoxMixin, DetailView):
    """
    Detail of a Box
    """
    login_url = '/admin/login/'
    model = Box
    template_name = 'box/detail.html'
    context_object_name = 'box'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(BOX_LIST_URL_NAME)
        if self.request.user.has_perm("app.change_box"):
            context['update_object_reversed_url'] = reverse_lazy(
                BOX_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("app.delete_box"):
            context['delete_object_reversed_url'] = reverse_lazy(
                BOX_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )
        return context


class Update(LoginRequiredMixin, BoxMixin, PermissionRequiredMixin, UpdateView):
    """
    Update a Box
    """
    login_url = '/admin/login/'
    model = Box
    template_name = 'box/update.html'
    context_object_name = 'box'
    form_class = BoxForm
    permission_required = (
        'app.change_box'
    )

    def get_initial(self):
        data = super(Update, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy(BOX_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_context_data(self, **kwargs):
        data = super(Update, self).get_context_data(**kwargs)
        data['list_reversed_url'] = reverse_lazy(BOX_LIST_URL_NAME)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Box atualizado com sucesso')
        return super(Update, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Update, self).form_invalid(form)


class Delete(LoginRequiredMixin, BoxMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete a Box
    """
    login_url = '/admin/login/'
    model = Box
    permission_required = (
        'app.delete_box'
    )
    template_name = 'box/delete.html'
    context_object_name = 'box'

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(BOX_LIST_URL_NAME)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(Delete, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Box removido com sucesso')
        return super(Delete, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(BOX_LIST_URL_NAME)
