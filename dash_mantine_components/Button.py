# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Button(Component):
    """A Button component.
ton

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Button content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- autoContrast (boolean; optional):
    Determines whether button text color with filled variant should
    depend on `background-color`. If luminosity of the `color` prop is
    less than `theme.luminosityThreshold`, then `theme.white` will be
    used for text color, otherwise `theme.black`. Overrides
    `theme.autoContrast`.

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
    Key of `theme.colors` or any valid CSS color, `theme.primaryColor`
    by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- disabled (boolean; optional):
    Indicates disabled state.

- display (boolean | number | string | dict | list; optional)

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional)

- fullWidth (boolean; optional):
    Determines whether button should take 100% width of its parent
    container, `False` by default.

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- gradient (dict; optional):
    Gradient configuration used when `variant=\"gradient\"`, default
    value is `theme.defaultGradient`.

    `gradient` is a dict with keys:

    - deg (number; optional)

    - from (string; required)

    - to (string; required)

- h (string | number; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inset (string | number; optional)

- justify (boolean | number | string | dict | list; optional):
    Sets `justify-content` of `inner` element, can be used to change
    distribution of sections and label, `'center'` by default.

- left (string | number; optional)

- leftSection (a list of or a singular dash component, string or number; optional):
    Content displayed on the left side of the button label.

- lh (number; optional)

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- loaderProps (dict; optional):
    Props added to the `Loader` component (only visible when `loading`
    prop is set).

    `loaderProps` is a dict with keys:

    - bd (string | number; optional)

    - bg (boolean | number | string | dict | list; optional)

    - bga (boolean | number | string | dict | list; optional)

    - bgp (string | number; optional)

    - bgr (boolean | number | string | dict | list; optional)

    - bgsz (string | number; optional)

    - bottom (string | number; optional)

    - c (boolean | number | string | dict | list; optional)

    - children (a list of or a singular dash component, string or number; optional):
        Overrides default loader with given content.

    - className (string; optional):
        Class added to the root element, if applicable.

    - classNames (dict; optional):
        Adds class names to Mantine components.

    - color (boolean | number | string | dict | list; optional):
        Key of `theme.colors` or any valid CSS color, default value is
        `theme.primaryColor`.

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

    - size (number; optional):
        Controls `width` and `height` of the loader. `Loader` has
        predefined `xs`-`xl` values. Numbers are converted to rem.
        Default value is `'md'`.

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - styles (boolean | number | string | dict | list; optional):
        Mantine styles API.

    - ta (boolean | number | string | dict | list; optional)

    - td (string | number; optional)

    - top (string | number; optional)

    - tt (boolean | number | string | dict | list; optional)

    - type (a value equal to: 'bars', 'dots', 'oval'; optional):
        Loader type, key of `loaders` prop, default value is `'oval'`.

    - unstyled (boolean; optional):
        Remove all Mantine styling from the component.

    - variant (string; optional):
        variant.

    - visibleFrom (boolean | number | string | dict | list; optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - w (string | number; optional)

- loading (boolean; optional):
    Determines whether the `Loader` component should be displayed over
    the button.

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

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

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

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, `theme.defaultRadius` by default.

- right (string | number; optional)

- rightSection (a list of or a singular dash component, string or number; optional):
    Content displayed on the right side of the button label.

- size (boolean | number | string | dict | list; optional):
    Controls button `height`, `font-size` and horizontal `padding`,
    `'sm'` by default.

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

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)"""
    _children_props = ['leftSection', 'rightSection', 'loaderProps.children']
    _base_nodes = ['leftSection', 'rightSection', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Button'
    @_explicitize_args
    def __init__(self, children=None, size=Component.UNDEFINED, color=Component.UNDEFINED, justify=Component.UNDEFINED, leftSection=Component.UNDEFINED, rightSection=Component.UNDEFINED, fullWidth=Component.UNDEFINED, radius=Component.UNDEFINED, gradient=Component.UNDEFINED, disabled=Component.UNDEFINED, loading=Component.UNDEFINED, loaderProps=Component.UNDEFINED, autoContrast=Component.UNDEFINED, n_clicks=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'autoContrast', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'darkHidden', 'data-*', 'disabled', 'display', 'ff', 'flex', 'fs', 'fullWidth', 'fw', 'fz', 'gradient', 'h', 'hiddenFrom', 'inset', 'justify', 'left', 'leftSection', 'lh', 'lightHidden', 'loaderProps', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_clicks', 'opacity', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'rightSection', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'autoContrast', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'darkHidden', 'data-*', 'disabled', 'display', 'ff', 'flex', 'fs', 'fullWidth', 'fw', 'fz', 'gradient', 'h', 'hiddenFrom', 'inset', 'justify', 'left', 'leftSection', 'lh', 'lightHidden', 'loaderProps', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_clicks', 'opacity', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'right', 'rightSection', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Button, self).__init__(children=children, **args)
