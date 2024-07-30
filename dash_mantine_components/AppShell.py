# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AppShell(Component):
    """An AppShell component.
Shell

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    Content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- aside (dict; optional):
    AppShell.Aside configuration, controls width, breakpoints and
    collapsed state. Required if you use AppShell.Aside component.

    `aside` is a dict with keys:

    - breakpoint (number; required)

    - collapsed (dict; optional)

        `collapsed` is a dict with keys:

        - desktop (boolean; optional)

        - mobile (boolean; optional)

    - width (number; required)

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
    If set, Navbar, Aside, Header and Footer components be hidden.

- display (boolean | number | string | dict | list; optional)

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- footer (dict; optional):
    AppShell.Footer configuration, controls height, offset and
    collapsed state. Required if you use AppShell.Footer component.

    `footer` is a dict with keys:

    - collapsed (boolean; optional)

    - height (number; required)

    - offset (boolean; optional)

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- h (string | number; optional)

- header (dict; optional):
    AppShell.Header configuration, controls height, offset and
    collapsed state. Required if you use AppShell.Header component.

    `header` is a dict with keys:

    - collapsed (boolean; optional)

    - height (number; required)

    - offset (boolean; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inset (string | number; optional)

- layout (a value equal to: 'default', 'alt'; optional):
    Determines how Navbar/Aside are arranged relative to
    Header/Footer, `default` by default.

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

- navbar (dict; optional):
    AppShell.Navbar configuration, controls width, breakpoints and
    collapsed state. Required if you use AppShell.Navbar component.

    `navbar` is a dict with keys:

    - breakpoint (number; required)

    - collapsed (dict; optional)

        `collapsed` is a dict with keys:

        - desktop (boolean; optional)

        - mobile (boolean; optional)

    - width (number; required)

- offsetScrollbars (boolean; optional):
    Determines whether Header and Footer components should include
    styles to offset scrollbars. Based on `react-remove-scroll`.
    `True` by default.

- opacity (boolean | number | string | dict | list; optional)

- p (number; optional)

- padding (number; optional):
    Controls padding of the main section, `0` by default. !important!:
    use `padding` prop instead of `p`.

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
    Duration of all transitions in ms, `200` by default.

- transitionTimingFunction (boolean | number | string | dict | list; optional):
    Timing function of all transitions, `ease` by default.

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withBorder (boolean; optional):
    Determines whether associated components should have a border,
    `True` by default.

- zIndex (string | number; optional):
    `z-index` of all associated elements, `200` by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'AppShell'
    @_explicitize_args
    def __init__(self, children=None, withBorder=Component.UNDEFINED, padding=Component.UNDEFINED, navbar=Component.UNDEFINED, aside=Component.UNDEFINED, header=Component.UNDEFINED, footer=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, zIndex=Component.UNDEFINED, layout=Component.UNDEFINED, disabled=Component.UNDEFINED, offsetScrollbars=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'aside', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'darkHidden', 'data-*', 'disabled', 'display', 'ff', 'flex', 'footer', 'fs', 'fw', 'fz', 'h', 'header', 'hiddenFrom', 'inset', 'layout', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'navbar', 'offsetScrollbars', 'opacity', 'p', 'padding', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withBorder', 'zIndex']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'aside', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'darkHidden', 'data-*', 'disabled', 'display', 'ff', 'flex', 'footer', 'fs', 'fw', 'fz', 'h', 'header', 'hiddenFrom', 'inset', 'layout', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'navbar', 'offsetScrollbars', 'opacity', 'p', 'padding', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withBorder', 'zIndex']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(AppShell, self).__init__(children=children, **args)
