# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ScatterChart(Component):
    """A ScatterChart component.
tterChart

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

- clickData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Click data.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (list of dicts; required):
    Data that is used to build the chart.

    `data` is a list of dicts with keys:

    - color (boolean | number | string | dict | list; required)

    - data (list of dicts; required)

        `data` is a list of dicts with keys:


    - name (string; required)

- data-* (string; optional):
    Wild card data attributes.

- dataKey (dict; required):
    Keys that should be used to retrieve data from the data array on x
    and y axis.

    `dataKey` is a dict with keys:

    - x (string; required)

    - y (string; required)

- display (boolean | number | string | dict | list; optional)

- ff (boolean | number | string | dict | list; optional)

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- gridAxis (a value equal to: 'none', 'x', 'y', 'xy'; optional):
    Specifies which lines should be displayed in the grid, `'x'` by
    default.

- gridColor (boolean | number | string | dict | list; optional):
    Color of the grid and cursor lines, by default depends on color
    scheme.

- gridProps (dict; optional):
    Props passed down to the `CartesianGrid` component.

- h (string | number; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inset (string | number; optional)

- labels (dict; optional):
    Labels that should be used instead of keys names in the tooltip.

    `labels` is a dict with keys:

    - x (string; optional)

    - y (string; optional)

- left (string | number; optional)

- legendProps (dict; optional):
    Props passed down to the `Legend` component.

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

- orientation (a value equal to: 'horizontal', 'vertical'; optional):
    Chart orientation, `'horizontal'` by default.

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

- referenceLines (list of dicts; optional):
    Reference lines that should be displayed on the chart.

- right (string | number; optional)

- scatterChartProps (dict; optional):
    Props passed down to recharts `ScatterChart` component.

- scatterProps (dict; optional):
    Props passed down to recharts `Scatter` component.

- strokeDasharray (string | number; optional):
    Dash array for the grid lines and cursor, `'5 5'` by default.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- textColor (boolean | number | string | dict | list; optional):
    Color of the text displayed inside the chart, `'dimmed'` by
    default.

- tickLine (a value equal to: 'none', 'x', 'y', 'xy'; optional):
    Specifies which axis should have tick line, `'y'` by default.

- tooltipAnimationDuration (number; optional):
    Tooltip position animation duration in ms, `0` by default.

- tooltipProps (dict; optional):
    Props passed down to the `Tooltip` component.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional)

- unit (dict; optional):
    Units displayed after value on axis and inside the tooltip.

    `unit` is a dict with keys:

    - x (string; optional)

    - y (string; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withLegend (boolean; optional):
    Determines whether chart legend should be displayed, `False` by
    default.

- withTooltip (boolean; optional):
    Determines whether chart tooltip should be displayed, `True` by
    default.

- withXAxis (boolean; optional):
    Determines whether x-axis should be hidden, `True` by default.

- withYAxis (boolean; optional):
    Determines whether y-axis should be hidden, `True` by default.

- xAxisLabel (string; optional):
    A label to display below the x-axis.

- xAxisProps (dict; optional):
    Props passed down to the `XAxis` recharts component.

- yAxisLabel (string; optional):
    A label to display next to the y-axis.

- yAxisProps (dict; optional):
    Props passed down to the `YAxis` recharts component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'ScatterChart'
    @_explicitize_args
    def __init__(self, dataKey=Component.REQUIRED, data=Component.REQUIRED, unit=Component.UNDEFINED, labels=Component.UNDEFINED, scatterChartProps=Component.UNDEFINED, scatterProps=Component.UNDEFINED, clickData=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, referenceLines=Component.UNDEFINED, withXAxis=Component.UNDEFINED, withYAxis=Component.UNDEFINED, xAxisProps=Component.UNDEFINED, yAxisProps=Component.UNDEFINED, gridProps=Component.UNDEFINED, tickLine=Component.UNDEFINED, strokeDasharray=Component.UNDEFINED, gridAxis=Component.UNDEFINED, tooltipAnimationDuration=Component.UNDEFINED, legendProps=Component.UNDEFINED, tooltipProps=Component.UNDEFINED, withLegend=Component.UNDEFINED, withTooltip=Component.UNDEFINED, textColor=Component.UNDEFINED, gridColor=Component.UNDEFINED, orientation=Component.UNDEFINED, xAxisLabel=Component.UNDEFINED, yAxisLabel=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'gridAxis', 'gridColor', 'gridProps', 'h', 'hiddenFrom', 'inset', 'labels', 'left', 'legendProps', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'referenceLines', 'right', 'scatterChartProps', 'scatterProps', 'strokeDasharray', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'tickLine', 'tooltipAnimationDuration', 'tooltipProps', 'top', 'tt', 'unit', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLegend', 'withTooltip', 'withXAxis', 'withYAxis', 'xAxisLabel', 'xAxisProps', 'yAxisLabel', 'yAxisProps']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'gridAxis', 'gridColor', 'gridProps', 'h', 'hiddenFrom', 'inset', 'labels', 'left', 'legendProps', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'referenceLines', 'right', 'scatterChartProps', 'scatterProps', 'strokeDasharray', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'tickLine', 'tooltipAnimationDuration', 'tooltipProps', 'top', 'tt', 'unit', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLegend', 'withTooltip', 'withXAxis', 'withYAxis', 'xAxisLabel', 'xAxisProps', 'yAxisLabel', 'yAxisProps']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'dataKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ScatterChart, self).__init__(**args)
