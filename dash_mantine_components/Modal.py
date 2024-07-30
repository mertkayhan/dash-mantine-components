# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modal(Component):
    """A Modal component.
al

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Modal content.

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

- centered (boolean; optional):
    Determines whether the modal should be centered vertically,
    `False` by default.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- closeButtonProps (dict; optional):
    Props passed down to the close button.

    `closeButtonProps` is a dict with keys:

    - bd (string | number; optional)

    - bg (boolean | number | string | dict | list; optional)

    - bga (boolean | number | string | dict | list; optional)

    - bgp (string | number; optional)

    - bgr (boolean | number | string | dict | list; optional)

    - bgsz (string | number; optional)

    - bottom (string | number; optional)

    - c (boolean | number | string | dict | list; optional)

    - children (a list of or a singular dash component, string or number; optional):
        Content rendered inside the button, for example
        `VisuallyHidden` with label for screen readers.

    - className (string; optional):
        Class added to the root element, if applicable.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - disabled (boolean; optional):
        Sets `disabled` and `data-disabled` attributes on the button
        element.

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

    - icon (a list of or a singular dash component, string or number; optional):
        Replaces default close icon. If set, `iconSize` prop is
        ignored.

    - iconSize (string | number; optional):
        `X` icon `width` and `height`, `80%` by default.

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

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius. Numbers are converted to rem.
        `theme.defaultRadius` by default.

    - right (string | number; optional)

    - size (number; optional):
        Controls width and height of the button. Numbers are converted
        to rem. `'md'` by default.

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

- closeOnClickOutside (boolean; optional):
    Determines whether the modal/drawer should be closed when user
    clicks on the overlay, `True` by default.

- closeOnEscape (boolean; optional):
    Determines whether `onClose` should be called when user presses
    the escape key, `True` by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- display (boolean | number | string | dict | list; optional)

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional)

- fullScreen (boolean; optional):
    Determines whether the modal should take the entire screen,
    `False` by default.

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- h (string | number; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inset (string | number; optional)

- keepMounted (boolean; optional):
    If set modal/drawer will not be unmounted from the DOM when it is
    hidden, `display: none` styles will be added instead, `False` by
    default.

- left (string | number; optional)

- lh (number; optional)

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- lockScroll (boolean; optional):
    Determines whether scroll should be locked when `opened={True}`,
    `True` by default.

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

- opened (boolean; default False):
    Determines whether modal/drawer is opened.

- overlayProps (dict; optional):
    Props passed down to the `Overlay` component, use to configure
    opacity, `background-color`, styles and other properties.

    `overlayProps` is a dict with keys:

    - backgroundOpacity (number; optional):
        Controls overlay `background-color` opacity 0–1, disregarded
        when `gradient` prop is set, `0.6` by default.

    - bd (string | number; optional)

    - bg (boolean | number | string | dict | list; optional)

    - bga (boolean | number | string | dict | list; optional)

    - bgp (string | number; optional)

    - bgr (boolean | number | string | dict | list; optional)

    - bgsz (string | number; optional)

    - blur (string | number; optional):
        Overlay background blur, `0` by default.

    - bottom (string | number; optional)

    - c (boolean | number | string | dict | list; optional)

    - center (boolean; optional):
        Determines whether content inside overlay should be vertically
        and horizontally centered, `False` by default.

    - children (a list of or a singular dash component, string or number; optional):
        Content inside overlay.

    - className (string; optional):
        Class added to the root element, if applicable.

    - color (boolean | number | string | dict | list; optional):
        Overlay `background-color`, `#000` by default.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - display (boolean | number | string | dict | list; optional)

    - ff (boolean | number | string | dict | list; optional)

    - fixed (boolean; optional):
        Determines whether overlay should have fixed position instead
        of absolute, `False` by default.

    - flex (string | number; optional)

    - fs (boolean | number | string | dict | list; optional)

    - fw (boolean | number | string | dict | list; optional)

    - fz (number; optional)

    - gradient (string; optional):
        Changes overlay to gradient. If set, `color` prop is ignored.

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

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius, `0` by default.

    - right (string | number; optional)

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - ta (boolean | number | string | dict | list; optional)

    - td (string | number; optional)

    - top (string | number; optional)

    - transitionProps (dict; optional):
        Props passed down to the `Transition` component.

        `transitionProps` is a dict with keys:

        - duration (number; optional):
            Transition duration in ms, `250` by default.

        - exitDuration (number; optional):
            Exit transition duration in ms, `250` by default.

        - keepMounted (boolean; optional):
            If set element will not be unmounted from the DOM when it
            is hidden, `display: none` styles will be applied instead.

        - mounted (boolean; required):
            Determines whether component should be mounted to the DOM.

        - timingFunction (string; optional):
            Transition timing function,
            `theme.transitionTimingFunction` by default.

        - transition (boolean | number | string | dict | list; optional):
            Transition name or object.

    - tt (boolean | number | string | dict | list; optional)

    - unstyled (boolean; optional):
        Remove all Mantine styling from the component.

    - visibleFrom (boolean | number | string | dict | list; optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - w (string | number; optional)

    - zIndex (string | number; optional):
        Overlay z-index, `200` by default.

- p (number; optional)

- padding (number; optional):
    Key of `theme.spacing` or any valid CSS value to set content,
    header and footer padding, `'md'` by default.

- pb (number; optional)

- pe (number; optional)

- pl (number; optional)

- portalProps (dict; optional):
    Props passed down to the Portal component when `withinPortal` is
    set.

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, `theme.defaultRadius` by default.

- removeScrollProps (dict; optional):
    Props passed down to react-remove-scroll, can be used to customize
    scroll lock behavior.

- returnFocus (boolean; optional):
    Determines whether focus should be returned to the last active
    element when `onClose` is called, `True` by default.

- right (string | number; optional)

- shadow (boolean | number | string | dict | list; optional):
    Key of `theme.shadows` or any valid CSS box-shadow value, 'xl' by
    default.

- size (number; optional):
    Controls width of the content area, `'md'` by default.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- title (a list of or a singular dash component, string or number; optional):
    Modal title.

- top (string | number; optional)

- transitionProps (dict; optional):
    Props added to the `Transition` component that used to animate
    overlay and body, use to configure duration and animation type, `{
    duration: 200, transition: 'pop' }` by default.

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

- trapFocus (boolean; optional):
    Determines whether focus should be trapped, `True` by default.

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withCloseButton (boolean; optional):
    Determines whether the close button should be rendered, `True` by
    default.

- withOverlay (boolean; optional):
    Determines whether the overlay should be rendered, `True` by
    default.

- withinPortal (boolean; optional):
    Determines whether the component should be rendered inside
    `Portal`, `True` by default.

- xOffset (string | number; optional):
    Left/right modal offset, `5vw` by default.

- yOffset (string | number; optional):
    Top/bottom modal offset, `5dvh` by default.

- zIndex (string | number; optional):
    `z-index` CSS property of the root element, `200` by default."""
    _children_props = ['title', 'overlayProps.children', 'closeButtonProps.children', 'closeButtonProps.icon']
    _base_nodes = ['title', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Modal'
    @_explicitize_args
    def __init__(self, children=None, title=Component.UNDEFINED, withOverlay=Component.UNDEFINED, overlayProps=Component.UNDEFINED, withCloseButton=Component.UNDEFINED, closeButtonProps=Component.UNDEFINED, yOffset=Component.UNDEFINED, xOffset=Component.UNDEFINED, radius=Component.UNDEFINED, centered=Component.UNDEFINED, fullScreen=Component.UNDEFINED, keepMounted=Component.UNDEFINED, opened=Component.UNDEFINED, lockScroll=Component.UNDEFINED, trapFocus=Component.UNDEFINED, withinPortal=Component.UNDEFINED, portalProps=Component.UNDEFINED, closeOnClickOutside=Component.UNDEFINED, transitionProps=Component.UNDEFINED, closeOnEscape=Component.UNDEFINED, returnFocus=Component.UNDEFINED, zIndex=Component.UNDEFINED, shadow=Component.UNDEFINED, padding=Component.UNDEFINED, size=Component.UNDEFINED, removeScrollProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'centered', 'className', 'classNames', 'closeButtonProps', 'closeOnClickOutside', 'closeOnEscape', 'darkHidden', 'data-*', 'display', 'ff', 'flex', 'fs', 'fullScreen', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'keepMounted', 'left', 'lh', 'lightHidden', 'lockScroll', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'opened', 'overlayProps', 'p', 'padding', 'pb', 'pe', 'pl', 'portalProps', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'removeScrollProps', 'returnFocus', 'right', 'shadow', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'title', 'top', 'transitionProps', 'trapFocus', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withCloseButton', 'withOverlay', 'withinPortal', 'xOffset', 'yOffset', 'zIndex']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'centered', 'className', 'classNames', 'closeButtonProps', 'closeOnClickOutside', 'closeOnEscape', 'darkHidden', 'data-*', 'display', 'ff', 'flex', 'fs', 'fullScreen', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'keepMounted', 'left', 'lh', 'lightHidden', 'lockScroll', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'opened', 'overlayProps', 'p', 'padding', 'pb', 'pe', 'pl', 'portalProps', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'removeScrollProps', 'returnFocus', 'right', 'shadow', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'title', 'top', 'transitionProps', 'trapFocus', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withCloseButton', 'withOverlay', 'withinPortal', 'xOffset', 'yOffset', 'zIndex']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Modal, self).__init__(children=children, **args)
