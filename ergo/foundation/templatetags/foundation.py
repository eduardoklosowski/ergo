# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static


register = template.Library()


@register.simple_tag
def foundation_css():
    return '<link rel="stylesheet" href="%s">' % static('foundation/css/foundation.css')


@register.simple_tag
def foundation_css_normalize():
    return '<link rel="stylesheet" href="%s">' % static('foundation/css/normalize.css')


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


@register.simple_tag
def foundation_js():
    return '<script src="%s"></script>' % static('foundation/js/foundation.min.js') + \
           '<script>$(document).foundation();</script>'


@register.simple_tag
def foundation_js_jquery():
    return '<script src="%s"></script>' % static('foundation/js/vendor/jquery.js')


@register.simple_tag
def foundation_js_modernizr():
    return '<script src="%s"></script>' % static('foundation/js/vendor/modernizr.js')


@register.simple_tag
def foundation_viewport():
    return '<meta name="viewport" contenet="width=device-width, initial-scale=1.0">'
