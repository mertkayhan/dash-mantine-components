# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Carousel(Component):
    """A Carousel component.
ousel

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    <Carousel.Slide /> components.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- align (number; optional):
    Determines how slides will be aligned relative to the container.
    Use number between 0-1 to align slides based on percentage, where
    0.5 is 50%, `'center'` by default.

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

- containScroll (a value equal to: '', 'trimSnaps', 'keepSnaps'; optional):
    Clear leading and trailing empty space that causes excessive
    scrolling. Use `trimSnaps` to only use snap points that trigger
    scrolling or keepSnaps to keep them.

- controlSize (string | number; optional):
    Controls size of the next and previous controls, `26` by default.

- controlsOffset (number; optional):
    Controls position of the next and previous controls, key of
    `theme.spacing` or any valid CSS value, `'sm'` by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- display (boolean | number | string | dict | list; optional)

- dragFree (boolean; optional):
    Determines whether momentum scrolling should be enabled, `False`
    by default.

- draggable (boolean; optional):
    Determines whether the carousel can be scrolled with mouse and
    touch interactions, `True` by default.

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- h (string | number; optional)

- height (string | number; optional):
    Slides container `height`, required for vertical orientation.

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inViewThreshold (number; optional):
    Choose a fraction representing the percentage portion of a slide
    that needs to be visible in order to be considered in view. For
    example, 0.5 equals 50%.

- includeGapInSize (boolean; optional):
    Determines whether gap between slides should be treated as part of
    the slide size, `True` by default.

- initialSlide (number; optional):
    Index of initial slide.

- inset (string | number; optional)

- left (string | number; optional)

- lh (number; optional)

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- loop (boolean; optional):
    Enables infinite looping. `True` by default, automatically falls
    back to `False` if slide content isn't enough to loop.

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

- nextControlIcon (a list of or a singular dash component, string or number; optional):
    Icon of the next control.

- opacity (boolean | number | string | dict | list; optional)

- orientation (a value equal to: 'horizontal', 'vertical'; optional):
    Carousel orientation, `'horizontal'` by default.

- p (number; optional)

- pb (number; optional)

- pe (number; optional)

- pl (number; optional)

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- previousControlIcon (a list of or a singular dash component, string or number; optional):
    Icon of the previous control.

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- right (string | number; optional)

- skipSnaps (boolean; optional):
    Allow the carousel to skip scroll snaps if it is dragged
    vigorously. Note that this option will be ignored if the dragFree
    option is set to `True`, `False` by default.

- slideGap (number; optional):
    Key of theme.spacing or number to set gap between slides.

- slideSize (string | number; optional):
    Controls slide width based on viewport width, `'100%'` by default.

- slidesToScroll (number; optional):
    Number of slides that will be scrolled with next/previous buttons,
    `1` by default.

- speed (number; optional):
    Adjusts scroll speed when triggered by any of the methods. Higher
    numbers enables faster scrolling.

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

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withControls (boolean; optional):
    Determines whether next/previous controls should be displayed,
    True by default.

- withIndicators (boolean; optional):
    Determines whether indicators should be displayed, `False` by
    default.

- withKeyboardEvents (boolean; optional):
    Determines whether arrow key should switch slides, `True` by
    default."""
    _children_props = ['nextControlIcon', 'previousControlIcon']
    _base_nodes = ['nextControlIcon', 'previousControlIcon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Carousel'
    @_explicitize_args
    def __init__(self, children=None, controlSize=Component.UNDEFINED, controlsOffset=Component.UNDEFINED, slideSize=Component.UNDEFINED, slideGap=Component.UNDEFINED, orientation=Component.UNDEFINED, height=Component.UNDEFINED, align=Component.UNDEFINED, slidesToScroll=Component.UNDEFINED, includeGapInSize=Component.UNDEFINED, draggable=Component.UNDEFINED, dragFree=Component.UNDEFINED, loop=Component.UNDEFINED, speed=Component.UNDEFINED, initialSlide=Component.UNDEFINED, inViewThreshold=Component.UNDEFINED, withControls=Component.UNDEFINED, withIndicators=Component.UNDEFINED, nextControlIcon=Component.UNDEFINED, previousControlIcon=Component.UNDEFINED, skipSnaps=Component.UNDEFINED, containScroll=Component.UNDEFINED, withKeyboardEvents=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'align', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'containScroll', 'controlSize', 'controlsOffset', 'darkHidden', 'data-*', 'display', 'dragFree', 'draggable', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'height', 'hiddenFrom', 'inViewThreshold', 'includeGapInSize', 'initialSlide', 'inset', 'left', 'lh', 'lightHidden', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'nextControlIcon', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'previousControlIcon', 'ps', 'pt', 'px', 'py', 'right', 'skipSnaps', 'slideGap', 'slideSize', 'slidesToScroll', 'speed', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withControls', 'withIndicators', 'withKeyboardEvents']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'align', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'containScroll', 'controlSize', 'controlsOffset', 'darkHidden', 'data-*', 'display', 'dragFree', 'draggable', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'height', 'hiddenFrom', 'inViewThreshold', 'includeGapInSize', 'initialSlide', 'inset', 'left', 'lh', 'lightHidden', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'nextControlIcon', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'previousControlIcon', 'ps', 'pt', 'px', 'py', 'right', 'skipSnaps', 'slideGap', 'slideSize', 'slidesToScroll', 'speed', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withControls', 'withIndicators', 'withKeyboardEvents']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Carousel, self).__init__(children=children, **args)
