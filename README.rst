###############
Jumpsuite Color Picker
###############

An addon to the Divio that provides a database and form
field to accept and store colors in the RGB format.

************
Installation
************


*****
Usage
*****

In order to use a color field you just have to add it to your model definition:

::

    from django.db import models
    from js_color_picker.fields import RGBColorField

    class Tag(models.Model):
        color = RGBColorField()

The ``RGBColorField`` class also accepts a ``color`` keyword argument which can
be set to a list(dict) of colors that should be visible as preset color palette
it replace JS_COLOR_PICKET_COLORS parameter in setings:

::

    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])

JS_COLOR_PICKET_COLORS or keyword colors shold be list of colors,
dics(keys are colors) or list of lists

::
    JS_COLOR_PICKET_COLORS = ['#FF0000', '#FF0000', '#FF0000']

or

::

    JS_COLOR_PICKET_COLORS = {
        "#FF0000": "Color 1",
        "#FF0000": "Color 2",
        "#FF0000": "Color 3",
    }

or

::

    JS_COLOR_PICKET_COLORS = [
        ["#FF0000", "Color 1"],
        ["#FF0000", "Color 2"],
        ["#FF0000", "Color 3"],
    ]


The ``RGBColorField`` class also accepts a ``mode`` keyword argument which can
be set to 'input', 'choice' and 'both'(default) it replace JS_COLOR_PICKET_MODE
parameter in setings:

::

    color = RGBColorField(mode='input')

The ``ColorFieldWidget`` should take care of providing a JavaScript based shim
on browsers that don't support the HTML5 color input.




