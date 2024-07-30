# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DonutChart(Component):
    """A DonutChart component.
utChart

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Additional elements rendered inside `PieChart` component.

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

- chartLabel (string | number; optional):
    Chart label, displayed in the center of the chart.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- clickData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Click data.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (list of dicts; required):
    Data used to render chart.

    `data` is a list of dicts with keys:

    - color (boolean | number | string | dict | list; required)

    - name (string; required)

    - value (number; required)

- data-* (string; optional):
    Wild card data attributes.

- display (boolean | number | string | dict | list; optional)

- endAngle (number; optional):
    Controls angle at which charts ends, `360` by default. Set to `0`
    to render the chart as semicircle.

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

- labelColor (boolean | number | string | dict | list; optional):
    Controls text color of all labels, by default depends on color
    scheme.

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

- mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- mr (number; optional)

- ms (number; optional)

- mt (number; optional)

- mx (number; optional)

- my (number; optional)

- opacity (boolean | number | string | dict | list; optional)

- p (number; optional)

- paddingAngle (number; optional):
    Controls padding between segments, `0` by default.

- pb (number; optional)

- pe (number; optional)

- pieChartProps (dict; optional):
    Props passed down to recharts `PieChart` component.

- pieProps (boolean | number | string | dict | list; optional):
    Props passed down to recharts `Pie` component.

- pl (number; optional)

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- right (string | number; optional)

- size (number; optional):
    Controls chart width and height, height is increased by 40 if
    `withLabels` prop is set. Cannot be less than `thickness`. `80` by
    default.

- startAngle (number; optional):
    Controls angle at which chart starts, `0` by default. Set to `180`
    to render the chart as semicircle.

- strokeColor (boolean | number | string | dict | list; optional):
    Controls color of the segments stroke, by default depends on color
    scheme.

- strokeWidth (number; optional):
    Controls width of segments stroke, `1` by default.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- thickness (number; optional):
    Controls thickness of the chart segments, `20` by default.

- tooltipAnimationDuration (number; optional):
    Tooltip animation duration in ms, `0` by default.

- tooltipDataSource (a value equal to: 'segment', 'all'; optional):
    Determines which data is displayed in the tooltip. `'all'` –
    display all values, `'segment'` – display only hovered segment.
    `'all'` by default.

- tooltipProps (boolean | number | string | dict | list; optional):
    Props passed down to `Tooltip` recharts component.

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

- withLabels (boolean; optional):
    Determines whether each segment should have associated label,
    `False` by default.

- withLabelsLine (boolean; optional):
    Determines whether segments labels should have lines that connect
    the segment with the label, `True` by default.

- withTooltip (boolean; optional):
    Determines whether the tooltip should be displayed when one of the
    section is hovered, `True` by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'DonutChart'
    @_explicitize_args
    def __init__(self, children=None, data=Component.REQUIRED, withTooltip=Component.UNDEFINED, tooltipAnimationDuration=Component.UNDEFINED, tooltipProps=Component.UNDEFINED, pieProps=Component.UNDEFINED, strokeColor=Component.UNDEFINED, labelColor=Component.UNDEFINED, paddingAngle=Component.UNDEFINED, withLabels=Component.UNDEFINED, withLabelsLine=Component.UNDEFINED, thickness=Component.UNDEFINED, size=Component.UNDEFINED, strokeWidth=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, tooltipDataSource=Component.UNDEFINED, chartLabel=Component.UNDEFINED, pieChartProps=Component.UNDEFINED, clickData=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chartLabel', 'className', 'classNames', 'clickData', 'darkHidden', 'data', 'data-*', 'display', 'endAngle', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'labelColor', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'paddingAngle', 'pb', 'pe', 'pieChartProps', 'pieProps', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'size', 'startAngle', 'strokeColor', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'thickness', 'tooltipAnimationDuration', 'tooltipDataSource', 'tooltipProps', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLabels', 'withLabelsLine', 'withTooltip']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chartLabel', 'className', 'classNames', 'clickData', 'darkHidden', 'data', 'data-*', 'display', 'endAngle', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'labelColor', 'left', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'paddingAngle', 'pb', 'pe', 'pieChartProps', 'pieProps', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'size', 'startAngle', 'strokeColor', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'thickness', 'tooltipAnimationDuration', 'tooltipDataSource', 'tooltipProps', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLabels', 'withLabelsLine', 'withTooltip']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DonutChart, self).__init__(children=children, **args)
