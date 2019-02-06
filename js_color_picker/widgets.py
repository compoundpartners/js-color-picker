from __future__ import unicode_literals

import json

from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.conf import settings


class ColorFieldWidget(TextInput):
    class Media:
        css = {
            'all': ("color-picker/color-picker.css",)
        }
        js = ("color-picker/color-picker.js",)

    input_type = 'text'

    def __init__(self, mode=None, colors=None, attrs=None):
        self.colors = colors or {}
        self.mode = mode or getattr(settings, 'JS_COLOR_PICKET_MODE', 'both')
        super(ColorFieldWidget, self).__init__(attrs)

    def render_colors(self):
        return json.dumps(self.colors)

    def render(self, name, value, renderer=None, attrs={}):
        parts = []
        if 'id' not in attrs:
            attrs['id'] = "id_%s" % name
        if self.colors:
            attrs['data-colors'] = self.render_colors()
        if self.mode in ['choice', 'both']:
            attrs['class'] = 'color-picker'
            if self.mode == 'choice':
                attrs['class'] += ' choice'
            else:
                attrs['class'] += ' add'
        parts.append(super(ColorFieldWidget, self).render(name, value, attrs))
        return mark_safe(''.join(parts))
