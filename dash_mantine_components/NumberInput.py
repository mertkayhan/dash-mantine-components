# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NumberInput(Component):
    """A NumberInput component.
berInput

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowDecimal (boolean; optional):
    Determines whether decimal values are allowed, `True` by default.

- allowLeadingZeros (boolean; optional):
    Determines whether leading zeros are allowed. If not set, leading
    zeros are removed when the input is blurred. `False` by default.

- allowNegative (boolean; optional):
    Determines whether negative values are allowed, `True` by default.

- allowedDecimalSeparators (list of strings; optional):
    Characters which when pressed result in a decimal separator,
    `['.']` by default.

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

- clampBehavior (a value equal to: 'none', 'strict', 'blur'; optional):
    Controls how value is clamped, `strict` – user is not allowed to
    enter values that are not in `[min, max]` range, `blur` – user is
    allowed to enter any values, but the value is clamped when the
    input loses focus (default behavior), `none` – lifts all
    restrictions, `[min, max]` range is applied only for controls and
    up/down keys.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- debounce (number; default 0):
    Debounce time in ms.

- decimalScale (number; optional):
    Limits the number of digits that can be entered after the decimal
    point.

- decimalSeparator (string; optional):
    Character used as a decimal separator, `'.'` by default.

- description (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Description` component. If not set, description
    is not rendered.

- descriptionProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Description` component.

- disabled (boolean; optional):
    Sets `disabled` attribute on the `input` element.

- display (boolean | number | string | dict | list; optional)

- error (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Error` component. If not set, error is not
    rendered.

- errorProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Error` component.

- ff (boolean | number | string | dict | list; optional)

- fixedDecimalScale (boolean; optional):
    If set, 0s are added after `decimalSeparator` to match given
    `decimalScale`. `False` by default.

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- h (string | number; optional)

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- hideControls (boolean; optional):
    Determines whether the up/down controls should be hidden, `False`
    by default.

- inputWrapperOrder (list of a value equal to: 'label', 'input', 'description', 'error's; optional):
    Controls order of the elements, `['label', 'description', 'input',
    'error']` by default.

- inset (string | number; optional)

- label (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Label` component. If not set, label is not
    rendered.

- labelProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Label` component.

- left (string | number; optional)

- leftSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the left side of the input.

- leftSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'none', 'auto', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `leftSection` element,
    `'none'` by default.

- leftSectionProps (dict; optional):
    Props passed down to the `leftSection` element.

- leftSectionWidth (string | number; optional):
    Left section width, used to set `width` of the section and input
    `padding-left`, by default equals to the input height.

- lh (number; optional)

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- lts (string | number; optional)

- m (number; optional)

- mah (string | number; optional)

- maw (string | number; optional)

- max (number; optional):
    Maximum possible value.

- mb (number; optional)

- me (number; optional)

- mih (string | number; optional)

- min (number; optional):
    Minimum possible value.

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

- n_submit (number; default 0):
    An integer that represents the number of times that this element
    has been submitted.

- name (string; optional):
    Name prop.

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

- placeholder (string; optional):
    Placeholder.

- pointer (boolean; optional):
    Determines whether the input should have `cursor: pointer` style,
    `False` by default.

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- prefix (string; optional):
    Prefix added before the input value.

- ps (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, numbers are converted to rem,
    `theme.defaultRadius` by default.

- readOnly (boolean; optional):
    Readonly.

- required (boolean; optional):
    Adds required attribute to the input and a red asterisk on the
    right side of label, `False` by default.

- right (string | number; optional)

- rightSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the right side of the input.

- rightSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'none', 'auto', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `rightSection` element,
    `'none'` by default.

- rightSectionProps (dict; optional):
    Props passed down to the `rightSection` element.

- rightSectionWidth (string | number; optional):
    Right section width, used to set `width` of the section and input
    `padding-right`, by default equals to the input height.

- size (boolean | number | string | dict | list; optional):
    Controls input `height` and horizontal `padding`, `'sm'` by
    default.

- startValue (number; optional):
    Value set to the input when increment/decrement buttons are
    clicked or up/down arrows pressed if the input is empty, `0` by
    default.

- step (number; optional):
    Number by which value will be incremented/decremented with up/down
    controls and keyboard arrows, `1` by default.

- stepHoldDelay (number; optional):
    Initial delay in milliseconds before stepping the value.

- stepHoldInterval (number; optional):
    Delay before stepping the value. Can be a number of milliseconds
    or a function that receives the current step count and returns the
    delay in milliseconds.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- suffix (string; optional):
    Suffix added after the input value.

- ta (boolean | number | string | dict | list; optional)

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional)

- thousandSeparator (string; optional):
    A character used to separate thousands.

- thousandsGroupStyle (a value equal to: 'none', 'thousand', 'lakh', 'wan'; optional):
    Defines the thousand grouping style.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional)

- type (a value equal to: 'text', 'tel', 'password'; optional):
    Controls input `type` attribute, `'text'` by default.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string | number; default ''):
    Controlled component value.

- valueIsNumericString (boolean; optional):
    If value is passed as string representation of numbers
    (unformatted) and number is used in any format props like in
    prefix or suffix in numeric format and format prop in pattern
    format then this should be passed as `True`. `False` by default.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional)

- withAsterisk (boolean; optional):
    Determines whether the required asterisk should be displayed.
    Overrides `required` prop. Does not add required attribute to the
    input. `False` by default.

- withErrorStyles (boolean; optional):
    Determines whether the input should have red border and red text
    color when the `error` prop is set, `True` by default.

- wrapperProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the root element."""
    _children_props = ['label', 'description', 'error', 'leftSection', 'rightSection']
    _base_nodes = ['label', 'description', 'error', 'leftSection', 'rightSection', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'NumberInput'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, allowLeadingZeros=Component.UNDEFINED, allowNegative=Component.UNDEFINED, allowedDecimalSeparators=Component.UNDEFINED, decimalScale=Component.UNDEFINED, decimalSeparator=Component.UNDEFINED, fixedDecimalScale=Component.UNDEFINED, prefix=Component.UNDEFINED, suffix=Component.UNDEFINED, thousandsGroupStyle=Component.UNDEFINED, valueIsNumericString=Component.UNDEFINED, type=Component.UNDEFINED, thousandSeparator=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, step=Component.UNDEFINED, hideControls=Component.UNDEFINED, clampBehavior=Component.UNDEFINED, allowDecimal=Component.UNDEFINED, startValue=Component.UNDEFINED, stepHoldInterval=Component.UNDEFINED, stepHoldDelay=Component.UNDEFINED, n_submit=Component.UNDEFINED, debounce=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, wrapperProps=Component.UNDEFINED, readOnly=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, error=Component.UNDEFINED, required=Component.UNDEFINED, withAsterisk=Component.UNDEFINED, labelProps=Component.UNDEFINED, descriptionProps=Component.UNDEFINED, errorProps=Component.UNDEFINED, inputWrapperOrder=Component.UNDEFINED, leftSection=Component.UNDEFINED, leftSectionWidth=Component.UNDEFINED, leftSectionProps=Component.UNDEFINED, leftSectionPointerEvents=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, rightSectionProps=Component.UNDEFINED, rightSectionPointerEvents=Component.UNDEFINED, radius=Component.UNDEFINED, disabled=Component.UNDEFINED, size=Component.UNDEFINED, pointer=Component.UNDEFINED, withErrorStyles=Component.UNDEFINED, placeholder=Component.UNDEFINED, name=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowDecimal', 'allowLeadingZeros', 'allowNegative', 'allowedDecimalSeparators', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'clampBehavior', 'className', 'classNames', 'darkHidden', 'data-*', 'debounce', 'decimalScale', 'decimalSeparator', 'description', 'descriptionProps', 'disabled', 'display', 'error', 'errorProps', 'ff', 'fixedDecimalScale', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hideControls', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'max', 'mb', 'me', 'mih', 'min', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_submit', 'name', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'pos', 'pr', 'prefix', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'startValue', 'step', 'stepHoldDelay', 'stepHoldInterval', 'style', 'styles', 'suffix', 'ta', 'tabIndex', 'td', 'thousandSeparator', 'thousandsGroupStyle', 'top', 'tt', 'type', 'unstyled', 'value', 'valueIsNumericString', 'variant', 'visibleFrom', 'w', 'withAsterisk', 'withErrorStyles', 'wrapperProps']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowDecimal', 'allowLeadingZeros', 'allowNegative', 'allowedDecimalSeparators', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'clampBehavior', 'className', 'classNames', 'darkHidden', 'data-*', 'debounce', 'decimalScale', 'decimalSeparator', 'description', 'descriptionProps', 'disabled', 'display', 'error', 'errorProps', 'ff', 'fixedDecimalScale', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hideControls', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'max', 'mb', 'me', 'mih', 'min', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_submit', 'name', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'pos', 'pr', 'prefix', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'startValue', 'step', 'stepHoldDelay', 'stepHoldInterval', 'style', 'styles', 'suffix', 'ta', 'tabIndex', 'td', 'thousandSeparator', 'thousandsGroupStyle', 'top', 'tt', 'type', 'unstyled', 'value', 'valueIsNumericString', 'variant', 'visibleFrom', 'w', 'withAsterisk', 'withErrorStyles', 'wrapperProps']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(NumberInput, self).__init__(**args)
