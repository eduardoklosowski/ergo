# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View


class DeleteView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        obj = get_object_or_404(self.model, **self.make_filter(request, pk))
        if request.GET.get('confirm', '') == 'y':
            obj.delete()
            messages.add_message(request, messages.INFO, self.message_deleted % {'title': self.title(obj)})
            if hasattr(self, 'redirect_args'):
                args = self.redirect_args(request, pk)
            else:
                args = []
            if hasattr(self, 'redirect_kwargs'):
                kwargs = self.redirect_kwargs(request, pk)
            else:
                kwargs = {}
            return redirect(self.redirect, *args, **kwargs)
        return render(request, 'ergohome/pag_delete.html', {
            'template': self.template,
            'title': self.message % {'title': self.title(obj)},
        })
