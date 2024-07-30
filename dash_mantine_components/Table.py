# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Table(Component):
    """A Table component.
le

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Headers, rows and footer.

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

- borderColor (boolean | number | string | dict | list; optional):
    Color of table borders, key of `theme.colors` or any valid CSS
    color.

- bottom (string | number; optional)

- c (boolean | number | string | dict | list; optional)

- captionSide (a value equal to: 'top', 'bottom'; optional):
    Determines on which side `Table.Caption` is displayed, `bottom` by
    default.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (dict; optional):
    Data that should be used to generate table, ignored if `children`
    prop is set.

    `data` is a dict with keys:

    - body (list of list of a list of or a singular dash component, string or numberss; optional)

    - caption (string; optional)

    - foot (list of a list of or a singular dash component, string or numbers; optional)

    - head (list of a list of or a singular dash component, string or numbers; optional)

- data-* (string; optional):
    Wild card data attributes.

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

- highlightOnHover (boolean; optional):
    Determines whether table rows background should change to
    `highlightOnHoverColor` when hovered, `False` by default.

- highlightOnHoverColor (boolean | number | string | dict | list; optional):
    Background color of table rows when hovered, key of `theme.colors`
    or any valid CSS color.

- horizontalSpacing (number; optional):
    Horizontal cells spacing, key of `theme.spacing` or any valid CSS
    value for padding, numbers are converted to rem, default value is
    `xs`.

- inset (string | number; optional)

- layout (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'auto', 'fixed'; optional):
    Value of `table-layout` style, `auto` by default.

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

- stickyHeader (boolean; optional):
    Determines whether `Table.Thead` should be sticky, `False` by
    default.

- stickyHeaderOffset (string | number; optional):
    Offset from top at which `Table.Thead` should become sticky, `0`
    by default.

- striped (boolean | number | string | dict | list; optional):
    Determines whether every odd/even row background should be changed
    to `strippedColor`, if set to `True`, then `odd` value will be
    used, `False` by default.

- stripedColor (boolean | number | string | dict | list; optional):
    Background color of striped rows, key of `theme.colors` or any
    valid CSS color.

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

- verticalSpacing (number; optional):
    Vertical cells spacing, key of `theme.spacing` or any valid CSS
    value for padding, numbers are converted to rem, default value is
    `xs`.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withColumnBorders (boolean; optional):
    Determines whether the table should have borders between columns,
    `False` by default.

- withRowBorders (boolean; optional):
    Determines whether the table should have borders between rows,
    `True` by default.

- withTableBorder (boolean; optional):
    Determines whether the table should have outer border, `False` by
    default."""
    _children_props = ['data.head', 'data.foot']
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Table'
    @_explicitize_args
    def __init__(self, children=None, layout=Component.UNDEFINED, captionSide=Component.UNDEFINED, borderColor=Component.UNDEFINED, withTableBorder=Component.UNDEFINED, withColumnBorders=Component.UNDEFINED, withRowBorders=Component.UNDEFINED, horizontalSpacing=Component.UNDEFINED, verticalSpacing=Component.UNDEFINED, striped=Component.UNDEFINED, stripedColor=Component.UNDEFINED, highlightOnHover=Component.UNDEFINED, highlightOnHoverColor=Component.UNDEFINED, data=Component.UNDEFINED, stickyHeader=Component.UNDEFINED, stickyHeaderOffset=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'borderColor', 'bottom', 'c', 'captionSide', 'className', 'classNames', 'darkHidden', 'data', 'data-*', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'highlightOnHover', 'highlightOnHoverColor', 'horizontalSpacing', 'inset', 'layout', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'stickyHeader', 'stickyHeaderOffset', 'striped', 'stripedColor', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'unstyled', 'variant', 'verticalSpacing', 'visibleFrom', 'w', 'withColumnBorders', 'withRowBorders', 'withTableBorder']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'borderColor', 'bottom', 'c', 'captionSide', 'className', 'classNames', 'darkHidden', 'data', 'data-*', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'highlightOnHover', 'highlightOnHoverColor', 'horizontalSpacing', 'inset', 'layout', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'stickyHeader', 'stickyHeaderOffset', 'striped', 'stripedColor', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'unstyled', 'variant', 'verticalSpacing', 'visibleFrom', 'w', 'withColumnBorders', 'withRowBorders', 'withTableBorder']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Table, self).__init__(children=children, **args)
