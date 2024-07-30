# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.
ltip

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    Target element, must support `ref` prop and `...others`.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- arrowOffset (number; optional):
    Arrow offset in px, `5` by default.

- arrowPosition (a value equal to: 'center', 'side'; optional):
    Arrow position relative to the tooltip, `side` by default.

- arrowRadius (number; optional):
    Arrow `border-radius` in px, `0` by default.

- arrowSize (number; optional):
    Arrow size in px, `4` by default.

- bd (string | number; optional)

- bg (boolean | number | string | dict | list; optional)

- bga (boolean | number | string | dict | list; optional)

- bgp (string | number; optional)

- bgr (boolean | number | string | dict | list; optional)

- bgsz (string | number; optional)

- bottom (string | number; optional)

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

    - w (string | number; optional)

- c (boolean | number | string | dict | list; optional)

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- closeDelay (number; optional):
    Close delay in ms, `0` by default.

- color (boolean | number | string | dict | list; optional):
    Key of `theme.colors` or any valid CSS color, controls tooltip
    background, by default set based on current color scheme.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- disabled (boolean; optional):
    If set, tooltip element will not be rendered.

- display (boolean | number | string | dict | list; optional)

- events (dict; optional):
    Determines which events will be used to show tooltip, `{ hover:
    True, focus: False, touch: False }` by default.

    `events` is a dict with keys:

    - focus (boolean; required)

    - hover (boolean; required)

    - touch (boolean; required)

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- floatingStrategy (a value equal to: 'fixed', 'absolute'; optional):
    Changes floating ui [position
    strategy](https://floating-ui.com/docs/usefloating#strategy),
    `'absolute'` by default.

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- h (string | number; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inline (boolean; optional):
    Must be set if the tooltip target is an inline element.

- inset (string | number; optional)

- keepMounted (boolean; optional):
    If set, the tooltip will not be unmounted from the DOM when it is
    hidden, `display: none` styles will be applied instead.

- label (a list of or a singular dash component, string or number; required):
    Tooltip content.

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

- multiline (boolean; optional):
    Determines whether content should be wrapped on to the next line,
    `False` by default.

- mx (number; optional)

- my (number; optional)

- offset (number; optional):
    Space between target element and tooltip in px, `5` by default.

- opacity (boolean | number | string | dict | list; optional)

- openDelay (number; optional):
    Open delay in ms.

- opened (boolean; optional):
    Controlled opened state.

- p (number; optional)

- pb (number; optional)

- pe (number; optional)

- pl (number; optional)

- portalProps (dict; optional):
    Props to pass down to the portal when withinPortal is True.

- pos (boolean | number | string | dict | list; optional)

- position (a value equal to: 'top', 'left', 'bottom', 'right', 'top-end', 'top-start', 'left-end', 'left-start', 'bottom-end', 'bottom-start', 'right-end', 'right-start'; optional):
    Tooltip position relative to target element (`Tooltip` component)
    or mouse (`Tooltip.Floating` component).

- positionDependencies (list of boolean | number | string | dict | lists; optional):
    `useEffect` dependencies to force update tooltip position.

- pr (number; optional)

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set border-radius,
    numbers are converted to rem, `theme.defaultRadius` by default.

- right (string | number; optional)

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

- transitionProps (dict; optional):
    Props passed down to the `Transition` component that used to
    animate tooltip presence, use to configure duration and animation
    type, `{ duration: 100, transition: 'fade' }` by default.

    `transitionProps` is a dict with keys:

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

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withArrow (boolean; optional):
    Determines whether the tooltip should have an arrow, `False` by
    default.

- withinPortal (boolean; optional):
    Determines whether tooltip should be rendered within `Portal`,
    `True` by default.

- zIndex (string | number; optional):
    Tooltip z-index, `300` by default."""
    _children_props = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Tooltip'
    @_explicitize_args
    def __init__(self, children=None, openDelay=Component.UNDEFINED, closeDelay=Component.UNDEFINED, opened=Component.UNDEFINED, offset=Component.UNDEFINED, withArrow=Component.UNDEFINED, arrowSize=Component.UNDEFINED, arrowOffset=Component.UNDEFINED, arrowRadius=Component.UNDEFINED, arrowPosition=Component.UNDEFINED, transitionProps=Component.UNDEFINED, events=Component.UNDEFINED, positionDependencies=Component.UNDEFINED, inline=Component.UNDEFINED, keepMounted=Component.UNDEFINED, floatingStrategy=Component.UNDEFINED, boxWrapperProps=Component.UNDEFINED, position=Component.UNDEFINED, label=Component.REQUIRED, withinPortal=Component.UNDEFINED, radius=Component.UNDEFINED, color=Component.UNDEFINED, multiline=Component.UNDEFINED, zIndex=Component.UNDEFINED, disabled=Component.UNDEFINED, portalProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'arrowOffset', 'arrowPosition', 'arrowRadius', 'arrowSize', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'boxWrapperProps', 'c', 'className', 'classNames', 'closeDelay', 'color', 'darkHidden', 'data-*', 'disabled', 'display', 'events', 'ff', 'flex', 'floatingStrategy', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inline', 'inset', 'keepMounted', 'label', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'multiline', 'mx', 'my', 'offset', 'opacity', 'openDelay', 'opened', 'p', 'pb', 'pe', 'pl', 'portalProps', 'pos', 'position', 'positionDependencies', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'transitionProps', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withArrow', 'withinPortal', 'zIndex']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'arrowOffset', 'arrowPosition', 'arrowRadius', 'arrowSize', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'boxWrapperProps', 'c', 'className', 'classNames', 'closeDelay', 'color', 'darkHidden', 'data-*', 'disabled', 'display', 'events', 'ff', 'flex', 'floatingStrategy', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inline', 'inset', 'keepMounted', 'label', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'multiline', 'mx', 'my', 'offset', 'opacity', 'openDelay', 'opened', 'p', 'pb', 'pe', 'pl', 'portalProps', 'pos', 'position', 'positionDependencies', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'transitionProps', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withArrow', 'withinPortal', 'zIndex']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(Tooltip, self).__init__(children=children, **args)
