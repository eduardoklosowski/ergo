# -*- coding: utf-8 -*-
#
# Copyright 2015 Eduardo Augusto Klosowski
#
# This file is part of Ergo.
#
# Ergo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ergo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Ergo.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import unicode_literals

from django import forms
from django import template


register = template.Library()


# Forms

@register.simple_tag
def foundation_form_hiddens(form):
    return ''.join(str(field) for field in form.hidden_fields())


@register.simple_tag
def foundation_form_errors(form):
    errors = form.non_field_errors()
    if errors:
        return '<small class="error">%s</small>' % errors
    return ''


@register.simple_tag
def foundation_form_field(field):
    if field.errors:
        label_class = 'error'
        field.field.widget.attrs['class'] = 'error'
        errors = '<small class="error">%s</small>' % field.errors
    else:
        label_class = ''
        errors = ''

    if isinstance(field.field.widget, forms.CheckboxInput):
        return ('<label class="%s" for="%s">%s:</label><div class="switch">%s<label for="%s"></label></div>%s' %
                (label_class, field.auto_id, field.label, field, field.auto_id, errors))

    return '<label class="%s">%s: %s</label>%s' % (label_class, field.label, field, errors)
