# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NumberFormatter(Component):
    """A NumberFormatter component.
berFormatter

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowNegative (boolean; optional):
    Determines whether negative values are allowed, `True` by default.

- aria-* (string; optional):
    Wild card aria attributes.

- data-* (string; optional):
    Wild card data attributes.

- decimalScale (number; optional):
    Limits the number of digits that are displayed after the decimal
    point, by default there is no limit.

- decimalSeparator (string; optional):
    Character used as a decimal separator, `'.'` by default.

- fixedDecimalScale (boolean; optional):
    If set, 0s are added after `decimalSeparator` to match given
    `decimalScale`. `False` by default.

- prefix (string; optional):
    Prefix added before the value.

- suffix (string; optional):
    Suffix added after the value.

- tabIndex (number; optional):
    tab-index.

- thousandSeparator (string; optional):
    A character used to separate thousands, `','` by default.

- thousandsGroupStyle (a value equal to: 'none', 'thousand', 'lakh', 'wan'; optional):
    Defines the thousand grouping style.

- value (string | number; optional):
    Value to format."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'NumberFormatter'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, allowNegative=Component.UNDEFINED, decimalScale=Component.UNDEFINED, decimalSeparator=Component.UNDEFINED, fixedDecimalScale=Component.UNDEFINED, prefix=Component.UNDEFINED, suffix=Component.UNDEFINED, thousandsGroupStyle=Component.UNDEFINED, thousandSeparator=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowNegative', 'aria-*', 'data-*', 'decimalScale', 'decimalSeparator', 'fixedDecimalScale', 'prefix', 'suffix', 'tabIndex', 'thousandSeparator', 'thousandsGroupStyle', 'value']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowNegative', 'aria-*', 'data-*', 'decimalScale', 'decimalSeparator', 'fixedDecimalScale', 'prefix', 'suffix', 'tabIndex', 'thousandSeparator', 'thousandsGroupStyle', 'value']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(NumberFormatter, self).__init__(**args)
