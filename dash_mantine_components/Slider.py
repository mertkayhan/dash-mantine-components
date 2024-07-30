# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Slider(Component):
    """A Slider component.
der

Keyword arguments:

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

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Key of `theme.colors` or any valid CSS color, controls color of
    track and thumb, `theme.primaryColor` by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- disabled (boolean; optional):
    Disables slider.

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

- inverted (boolean; optional):
    Determines whether track value representation should be inverted,
    `False` by default.

- label (a list of or a singular dash component, string or number; optional):
    Function to generate label or any react node to render instead,
    set to None to disable label.

- labelAlwaysOn (boolean; optional):
    Determines whether the label should be visible when the slider is
    not being dragged or hovered, `False` by default.

- labelTransitionProps (dict; optional):
    Props passed down to the `Transition` component, `{ transition:
    'fade', duration: 0 }` by default.

    `labelTransitionProps` is a dict with keys:

    - duration (number; optional):
        Transition duration in ms, `250` by default.

    - exitDuration (number; optional):
        Exit transition duration in ms, `250` by default.

    - keepMounted (boolean; optional):
        If set element will not be unmounted from the DOM when it is
        hidden, `display: none` styles will be applied instead.

    - mounted (boolean; required):
        Determines whether component should be mounted to the DOM.

    - timingFunction (string; optional):
        Transition timing function, `theme.transitionTimingFunction`
        by default.

    - transition (boolean | number | string | dict | list; optional):
        Transition name or object.

- left (string | number; optional)

- lh (number; optional)

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- lts (string | number; optional)

- m (number; optional)

- mah (string | number; optional)

- marks (list of dicts; optional):
    Marks displayed on the track.

    `marks` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional)

    - value (number; required)

- maw (string | number; optional)

- max (number; optional):
    Maximum possible value, `100` by default.

- mb (number; optional)

- me (number; optional)

- mih (string | number; optional)

- min (number; optional):
    Minimal possible value, `0` by default.

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

- name (string; optional):
    Hidden input name, use with uncontrolled component.

- opacity (boolean | number | string | dict | list; optional)

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

- precision (number; optional):
    Number of significant digits after the decimal point.

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, numbers are converted to rem, `'xl'` by default.

- right (string | number; optional)

- showLabelOnHover (boolean; optional):
    Determines whether the label should be displayed when the slider
    is hovered, `True` by default.

- size (number; optional):
    Controls size of the track, `'md'` by default.

- step (number; optional):
    Number by which value will be incremented/decremented with thumb
    drag and arrows, `1` by default.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- thumbChildren (a list of or a singular dash component, string or number; optional):
    Content rendered inside thumb.

- thumbLabel (string; optional):
    Thumb `aria-label`.

- thumbSize (string | number; optional):
    Thumb `width` and `height`, by default value is computed based on
    `size` prop.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- updatemode (a value equal to: 'mouseup', 'drag'; default 'mouseup'):
    Determines when the component should update its value property. If
    mouseup (the default) then the slider will only trigger its value
    when the user has finished dragging the slider. If drag, then the
    slider will update its value continuously as it is being dragged.

- value (number; optional):
    Controlled component value.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)"""
    _children_props = ['marks[].label', 'label', 'thumbChildren']
    _base_nodes = ['label', 'thumbChildren', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Slider'
    @_explicitize_args
    def __init__(self, color=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, step=Component.UNDEFINED, precision=Component.UNDEFINED, value=Component.UNDEFINED, name=Component.UNDEFINED, marks=Component.UNDEFINED, label=Component.UNDEFINED, labelTransitionProps=Component.UNDEFINED, labelAlwaysOn=Component.UNDEFINED, thumbLabel=Component.UNDEFINED, showLabelOnHover=Component.UNDEFINED, thumbChildren=Component.UNDEFINED, disabled=Component.UNDEFINED, thumbSize=Component.UNDEFINED, inverted=Component.UNDEFINED, updatemode=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'darkHidden', 'data-*', 'disabled', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'inverted', 'label', 'labelAlwaysOn', 'labelTransitionProps', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'marks', 'maw', 'max', 'mb', 'me', 'mih', 'min', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'name', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'precision', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'showLabelOnHover', 'size', 'step', 'style', 'styles', 'ta', 'tabIndex', 'td', 'thumbChildren', 'thumbLabel', 'thumbSize', 'top', 'tt', 'unstyled', 'updatemode', 'value', 'variant', 'visibleFrom', 'w']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'darkHidden', 'data-*', 'disabled', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'inverted', 'label', 'labelAlwaysOn', 'labelTransitionProps', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'marks', 'maw', 'max', 'mb', 'me', 'mih', 'min', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'name', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'precision', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'showLabelOnHover', 'size', 'step', 'style', 'styles', 'ta', 'tabIndex', 'td', 'thumbChildren', 'thumbLabel', 'thumbSize', 'top', 'tt', 'unstyled', 'updatemode', 'value', 'variant', 'visibleFrom', 'w']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Slider, self).__init__(**args)
