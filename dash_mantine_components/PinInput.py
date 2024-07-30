# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PinInput(Component):
    """A PinInput component.
Input

Keyword arguments:

- id (string; optional):
    Base id used for all inputs. By default, inputs' ids are generated
    randomly.

- aria-* (string; optional):
    Wild card aria attributes.

- ariaLabel (string; optional):
    `aria-label` for the inputs.

- autoFocus (boolean; optional):
    If set, the first input is focused when component is mounted,
    `False` by default.

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

- classNames (dict; optional):
    Adds class names to Mantine components.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- disabled (boolean; optional):
    If set, `disabled` attribute is added to all inputs.

- display (boolean | number | string | dict | list; optional)

- error (boolean; optional):
    If set, adds error styles and `aria-invalid` attribute to all
    inputs.

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- form (string; optional):
    Hidden input `form` attribute.

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- gap (number; optional):
    Key of `theme.spacing` or any valid CSS value to set `gap` between
    inputs, numbers are converted to rem, `'md'` by default.

- h (string | number; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inputMode (a value equal to: 'none', 'text', 'tel', 'email', 'search', 'url', 'numeric', 'decimal'; optional):
    `inputmode` attribute, inferred from the `type` prop if not
    specified.

- inputType (boolean | number | string | dict | list; optional):
    Inputs `type` attribute, inferred from the `type` prop if not
    specified.

- inset (string | number; optional)

- left (string | number; optional)

- length (number; optional):
    Number of inputs, `4` by default.

- lh (number; optional)

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- lts (string | number; optional)

- m (number; optional)

- mah (string | number; optional)

- manageFocus (boolean; optional):
    Determines whether focus should be moved automatically to the next
    input once filled, `True` by default.

- mask (boolean; optional):
    Changes input type to `\"password\"`, `False` by default.

- maw (string | number; optional)

- mb (number; optional)

- me (number; optional)

- mih (string | number; optional)

- miw (string | number; optional)

- ml (number; optional)

- mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- mr (number; optional)

- ms (number; optional)

- mt (number; optional)

- mx (number; optional)

- my (number; optional)

- name (string; optional):
    Hidden input `name` attribute.

- oneTimeCode (boolean; optional):
    Determines whether `autocomplete=\"one-time-code\"` attribute
    should be set on all inputs, `True` by default.

- opacity (boolean | number | string | dict | list; optional)

- p (number; optional)

- pb (number; optional)

- pe (number; optional)

- persisted_props (list of strings; optional):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pl (number; optional)

- placeholder (string; optional):
    Inputs placeholder, `'○'` by default.

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, numbers are converted to rem,
    `theme.defaultRadius` by default.

- readOnly (boolean; optional):
    If set, the user cannot edit the value.

- right (string | number; optional)

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Controls inputs `width` and `height`, `'sm'` by default.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional)

- type (boolean | number | string | dict | list; optional):
    Determines which values can be entered, `'alphanumeric'` by
    default.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string; optional):
    Controlled component value.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'PinInput'
    @_explicitize_args
    def __init__(self, name=Component.UNDEFINED, form=Component.UNDEFINED, gap=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, autoFocus=Component.UNDEFINED, value=Component.UNDEFINED, placeholder=Component.UNDEFINED, manageFocus=Component.UNDEFINED, oneTimeCode=Component.UNDEFINED, id=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, type=Component.UNDEFINED, mask=Component.UNDEFINED, length=Component.UNDEFINED, readOnly=Component.UNDEFINED, inputType=Component.UNDEFINED, inputMode=Component.UNDEFINED, ariaLabel=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, tabIndex=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aria-*', 'ariaLabel', 'autoFocus', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'darkHidden', 'data-*', 'disabled', 'display', 'error', 'ff', 'flex', 'form', 'fs', 'fw', 'fz', 'gap', 'h', 'hiddenFrom', 'inputMode', 'inputType', 'inset', 'left', 'length', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'manageFocus', 'mask', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'name', 'oneTimeCode', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'right', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'type', 'unstyled', 'value', 'variant', 'visibleFrom', 'w']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'ariaLabel', 'autoFocus', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'darkHidden', 'data-*', 'disabled', 'display', 'error', 'ff', 'flex', 'form', 'fs', 'fw', 'fz', 'gap', 'h', 'hiddenFrom', 'inputMode', 'inputType', 'inset', 'left', 'length', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'manageFocus', 'mask', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'name', 'oneTimeCode', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'right', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'type', 'unstyled', 'value', 'variant', 'visibleFrom', 'w']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(PinInput, self).__init__(**args)
