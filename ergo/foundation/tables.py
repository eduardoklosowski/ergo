# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.template.loader import get_template
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Table(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return get_template('foundation/table.html').render({'table': self})

    def get_table_class(self):
        return getattr(self, 'table_class', 'width-full')

    def get_headers(self):
        headers = []
        for column in self.columns:
            headers.append({'name': column['name'],
                            'class': ('%s %s' % (column.get('header_class', ''), column.get('class', ''))).strip()})
        return headers

    def get_rows(self):
        rows = []
        for row in self.data:
            if hasattr(self, 'data_extra'):
                data = (row, self.data_extra)
            else:
                data = (row,)
            rows.append([{'class': ('%s %s' % (column.get('row_class', ''), column.get('class', ''))).strip(),
                          'value': column['value'](*data)} for column in self.columns])
        return rows
