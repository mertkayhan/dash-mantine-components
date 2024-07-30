# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Accordion(Component):
    """An Accordion component.
ordion

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    Accordion content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- bd (string | number; optional)

- bg (boolean | number | string | dict | list; optional)

- bga (boolean | number | string | dict | list; optional)

- bgp (string | number; optional)

- bgr (boolean | number | string | dict | list; optional)

- bgsz (string | number; optional)

- bottom (string | number; optional)

- c (boolean | number | string | dict | list; optional)

- chevron (a list of or a singular dash component, string or number; optional):
    Custom chevron icon that will be used in all items.

- chevronPosition (a value equal to: 'left', 'right'; optional):
    Position of the chevron relative to the item label, `right` by
    default.

- chevronSize (string | number; optional):
    Size of the chevron icon container, `24` by default.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- disableChevronRotation (boolean; optional):
    Determines whether chevron rotation should be disabled, `False` by
    default.

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

- loop (boolean; optional):
    Determines whether arrow key presses should loop though items
    (first to last and last to first), `True` by default.

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

- multiple (boolean; optional):
    Determines whether multiple items can be opened at a time, `False`
    by default.

- mx (number; optional)

- my (number; optional)

- opacity (boolean | number | string | dict | list; optional)

- order (a value equal to: 2, 3, 4, 5, 6; optional):
    Heading order, has no effect on visuals.

- p (number; optional)

- pb (number; optional)

- pe (number; optional)

- persisted_props (list of strings; default ["value"]):
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

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pl (number; optional)

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set border-radius.
    Numbers are converted to rem. `theme.defaultRadius` by default.

- right (string | number; optional)

- style (boolean | number | string | dict | list; optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- top (string | number; optional)

- transitionDuration (number; optional):
    Transition duration in ms, `200` by default.

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string | list of strings; optional):
    Value for controlled component.

- variant (a value equal to: 'default', 'contained', 'filled', 'separated'; optional):
    Controls visuals.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)"""
    _children_props = ['chevron']
    _base_nodes = ['chevron', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Accordion'
    @_explicitize_args
    def __init__(self, children=None, multiple=Component.UNDEFINED, value=Component.UNDEFINED, loop=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, disableChevronRotation=Component.UNDEFINED, chevronPosition=Component.UNDEFINED, chevronSize=Component.UNDEFINED, order=Component.UNDEFINED, chevron=Component.UNDEFINED, variant=Component.UNDEFINED, radius=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chevron', 'chevronPosition', 'chevronSize', 'className', 'classNames', 'darkHidden', 'data-*', 'disableChevronRotation', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'left', 'lh', 'lightHidden', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'multiple', 'mx', 'my', 'opacity', 'order', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'transitionDuration', 'tt', 'unstyled', 'value', 'variant', 'visibleFrom', 'w']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chevron', 'chevronPosition', 'chevronSize', 'className', 'classNames', 'darkHidden', 'data-*', 'disableChevronRotation', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'left', 'lh', 'lightHidden', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'multiple', 'mx', 'my', 'opacity', 'order', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'transitionDuration', 'tt', 'unstyled', 'value', 'variant', 'visibleFrom', 'w']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(Accordion, self).__init__(children=children, **args)
