# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static


include_css = '<link rel="stylesheet" href="%s">'
include_js = '<script src="%s"></script>'
register = template.Library()


@register.simple_tag
def foundation_viewport():
    return '<meta name="viewport" contenet="width=device-width, initial-scale=1.0">'


@register.simple_tag
def foundation_css():
    return (include_css % static('foundation/css/normalize.css') +
            include_css % static('foundation/css/foundation.css'))


@register.simple_tag
def foundation_js():
    return (include_js % static('foundation/js/foundation.js') +
           '<script>$(document).foundation();</script>')


@register.simple_tag
def foundation_form_column_class(field):
    return field.form.foundation_column_class(field.name)


@register.simple_tag
def foundation_form_errors(form):
    erros = form.non_field_errors()
    if erros:
        return '<small class="error">%s</small>' % erros
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
        return '<label class="%s" for="%s">%s:</label><div class="switch">%s<label for="%s"></label></div>%s' % \
            (label_class, field.auto_id, field.label, field, field.auto_id, errors)

    return '<label class="%s">%s: %s</label>%s' % (label_class, field.label, field, errors)


@register.simple_tag
def foundation_form_hiddens(form):
    html = []
    for hidden in form.hidden_fields():
        html.append(str(hidden))
    return ''.join(html)
