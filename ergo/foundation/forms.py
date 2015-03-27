# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.template.loader import get_template


class FoundationForm(object):
    def as_foundation(self):
        return get_template('foundation/form.html').render({'form': self})

    def foundation_column_class(self, field):
        columns = getattr(self.Meta, 'foundation_column_class', {})
        return columns.get(field, 'small-12 medium-6') + ' columns'

    def foundation_fieldsets(self):
        if hasattr(self.Meta, 'foundation_fieldsets'):
            return [(name, [self[field] for field in fields])
                    for name, fields in self.Meta.foundation_fieldsets]

        return ((None, self.visible_fields()),)
