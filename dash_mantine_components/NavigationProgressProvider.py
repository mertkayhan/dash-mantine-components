# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NavigationProgressProvider(Component):
    """A NavigationProgressProvider component.
igationProgressProvider

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- color (boolean | number | string | dict | list; optional):
    Key of `theme.colors` of any other valid CSS color,
    `theme.primaryColor` by default.

- data-* (string; optional):
    Wild card data attributes.

- initialProgress (number; optional):
    Initial progress value, `0` by default.

- size (number; optional):
    Controls height of the progress bar.

- stepInterval (number; optional):
    Step interval in ms, `500` by default.

- tabIndex (number; optional):
    tab-index.

- withinPortal (boolean; optional):
    Determines whether the progress bar should be rendered within
    `Portal`, `True` by default.

- zIndex (boolean | number | string | dict | list; optional):
    Progressbar z-index, `9999` by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'NavigationProgressProvider'
    @_explicitize_args
    def __init__(self, initialProgress=Component.UNDEFINED, color=Component.UNDEFINED, size=Component.UNDEFINED, stepInterval=Component.UNDEFINED, withinPortal=Component.UNDEFINED, zIndex=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aria-*', 'color', 'data-*', 'initialProgress', 'size', 'stepInterval', 'tabIndex', 'withinPortal', 'zIndex']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'color', 'data-*', 'initialProgress', 'size', 'stepInterval', 'tabIndex', 'withinPortal', 'zIndex']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(NavigationProgressProvider, self).__init__(**args)
