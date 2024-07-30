# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PopoverTarget(Component):
    """A PopoverTarget component.
overTarget

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    Content.

- boxWrapperProps (dict; optional):
    Target box wrapper props.

    `boxWrapperProps` is a dict with keys:

    - bd (string | number; optional)

    - bg (boolean | number | string | dict | list; optional)

    - bga (boolean | number | string | dict | list; optional)

    - bgp (string | number; optional)

    - bgr (boolean | number | string | dict | list; optional)

    - bgsz (string | number; optional)

    - bottom (string | number; optional)

    - c (boolean | number | string | dict | list; optional)

    - className (string; optional):
        Class added to the root element, if applicable.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - display (boolean | number | string | dict | list; optional)

    - ff (boolean | number | string | dict | list; optional)

    - flex (string | number; optional)

    - fs (boolean | number | string | dict | list; optional)

    - fw (boolean | number | string | dict | list; optional)

    - fz (number; optional)

    - h (string | number; optional)

    - hiddenFrom (boolean | number | string | dict | list; optional):
        Breakpoint above which the component is hidden with `display:
        none`.

    - inset (string | number; optional)

    - left (string | number; optional)

    - lh (number; optional)

    - lightHidden (boolean; optional):
        Determines whether component should be hidden in light color
        scheme with `display: none`.

    - lts (string | number; optional)

    - m (number; optional)

    - mah (string | number; optional)

    - maw (string | number; optional)

    - mb (number; optional)

    - me (number; optional)

    - mih (string | number; optional)

    - miw (string | number; optional)

    - ml (number; optional)

    - mod (string; optional):
        Element modifiers transformed into `data-` attributes, for
        example, `{ 'data-size': 'xl' }`, falsy values are removed.

    - mr (number; optional)

    - ms (number; optional)

    - mt (number; optional)

    - mx (number; optional)

    - my (number; optional)

    - opacity (boolean | number | string | dict | list; optional)

    - p (number; optional)

    - pb (number; optional)

    - pe (number; optional)

    - pl (number; optional)

    - pos (boolean | number | string | dict | list; optional)

    - pr (number; optional)

    - ps (number; optional)

    - pt (number; optional)

    - px (number; optional)

    - py (number; optional)

    - right (string | number; optional)

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - ta (boolean | number | string | dict | list; optional)

    - td (string | number; optional)

    - top (string | number; optional)

    - tt (boolean | number | string | dict | list; optional)

    - visibleFrom (boolean | number | string | dict | list; optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - w (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'PopoverTarget'
    @_explicitize_args
    def __init__(self, children=None, boxWrapperProps=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'boxWrapperProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'boxWrapperProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(PopoverTarget, self).__init__(children=children, **args)
