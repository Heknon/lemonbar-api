# Lemonbar API

## Goal

Provide a simple to use, modern asynchronous Pythonic API for [Lemonbar](https://github.com/drscream/lemonbar-xft).

Grow upon the primitives that Lemonbar provides, to provide the end-user
of this library with extensive features.

## Getting Started

TODO

## How to use

### Creating a Lemonbar instance.

Firstly, you must create an instance of the Lemonbar class.

This class manages the low-level interactions with Lemonbar CLI and
abstracts them for you.

```python
from lemonbar import Lemonbar
from lemonbar.models import BarGeometry
from lemonbar.models.bar_placement import BarPlacement


async def main():
    lemonbar = Lemonbar(
        [
            # modules... (Talked about later)
        ],
        geometry=BarGeometry.build(height=50),
        placement=BarPlacement.BOTTOM,
        background_color="#111111",
        foreground_color="#B2B2B2",
        underline_color="#D8AD4C"
    )
    lemonbar.open()
    await lemonbar.attach()
```

Above, you see how you create the Lemonbar instance.

As you can see all the passing of CLI arguments is abstracted away from you
in a nice and clean fashion. To add on to that, all types passed are validated
using Pydantic - Including colors and screen outputs.
Unfortunately, validation could not be made for font names.

#### Arguments

Default values are passed according to Lemonbar specification.

All you need to do to have Lemonbar running is define modules!

`modules: List[Module]`

Modules are an interface that the `Lemonbar` class knows how to communicate with.

They allow you to efficiently render data on to a bar.

`geometry: BarGeometry = None`

Allows you to define the size and offsets of the bar on the screen.

`outputs: Optional[List[MonitorId]] = None`

Allows you to define the monitors which you'd like the Lemonbar to be
displayed on. If nothing is passed, it will display on all screens.

`placement: BarPlacement = BarPlacement.TOP`

Allows you to define whether you want the bar to be placed on the top
of your screen or on the bottom.

`force_dock: bool = False`

Force docking without asking the window manager.
This is needed if the window manager isn't EWMH compliant.

`fonts: Optional[List[str]] = None`

Define the font to load into one of the five slots
See: [Lemonbar Options](https://github.com/drscream/lemonbar-xft#options)

`permanent: bool = False`

Make the bar permanent, don't exit after the standard input is closed.

`title: Optional[str] = ""`

Defines the WM_NAME of the bar. Meaning the title of the window.

`underline_width: int = 1`

Sets the underline width in pixels. The default is 1.

`background_color: Optional[str] = None`

Set the background color of the bar.

Since Pydantic is used, any of the following is valid:
[Pydantic Color Extension](https://docs.pydantic.dev/latest/usage/types/extra_types/color_types/)

1. name (e.g. "Black", "azure")
2. hexadecimal value (e.g. "0x000", "#FFFFFF", "7fffd4")
3. RGB/RGBA tuples (e.g. (255, 255, 255), (255, 255, 255, 0.5))
4. RGB/RGBA strings (e.g. "rgb(255, 255, 255)", "rgba(255, 255, 255, 0.5)")
5. HSL strings (e.g. "hsl(270, 60%, 70%)", "hsl(270, 60%, 70%, .5)")

`foreground_color: Optional[str] = None`

Same as background color but for the foreground.

`underline_color: Optional[str] = None`

Same as background color but for underlines.

`logger: logging.Logger = _DEFAULT_LOGGER`

The logger the Lemonbar class should use when logging information about
the execution of modules.

## Modules

A module is simply a class which defines the following:

1. What string to render
2. When to render
3. How to handle events (stdout from Lemonbar)
4. When to handle events

See one of the predefined modules for an example.

For example: [Clock](https://github.com/Heknon/lemonbar-api/blob/master/modules/clock.py)

Modules also have the option to define a `Module Configuration`, a configuration
is made up of the following fields:

`minimum_render_interval: datetime.timedelta = datetime.timedelta(seconds=1)`

The minimum amount of time to wait before calling `render()` on the
module again.

This is a guarantee that after **at least** `timedelta`, in the
next render cycle, the `render` method is called.

`force_render_on_event: bool = True`

Allows you to override `minimum_render_interval`
if the module processed an event. Meaning, if `minimum_render_interval` has not
passed but the module processed an event, `render` will be called.

`cache_exceptions: bool = True`

If true and an exception is raised in the module,
do not try immediately on the next render cycle to re-render but
wait `minimum_render_interval`.

## Formatters

This library also provides formatters for those defined
[here](https://github.com/drscream/lemonbar-xft#formatting) under
the `formatters` package.

You are more than welcome to take a look at it!
