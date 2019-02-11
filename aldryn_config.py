from aldryn_client import forms

MODES = (
    ('', '-----------'),
    ('input', 'Text hex Color'),
    ('choice', 'Pre-set Color Dropdown'),
    ('both', 'Both'),
)

class Form(forms.BaseForm):
    colors = forms.CharField(
        'List of colors (comma separated)',
        required=False
    )
    mode = forms.SelectField(
        'Color picker mode',
        MODES,
        required=False,
    )

    def to_settings(self, data, settings):

        if data['colors']:
            settings['JS_COLOR_PICKET_COLORS'] = data['colors'].split(',')
        if data['mode']:
            settings['JS_COLOR_PICKET_MODE'] = data['mode']

        return settings
