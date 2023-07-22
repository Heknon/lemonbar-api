import asyncio

from modules.clock import Clock
from lemonbar import Lemonbar
from models.bar_geometry import BarGeometry
from models.bar_placement import BarPlacement


async def main():
    lemonbar = Lemonbar(
        [
            Clock(),
        ],
        geometry=BarGeometry.build(height=50),
        placement=BarPlacement.TOP,
        background_color="red",
        foreground_color="blue",
        underline_color="#D8AD4C",
        underline_width=2,
        fonts=["JetBrainsMono:size=18"],
    )
    lemonbar.open()
    await lemonbar.attach()


if __name__ == '__main__':
    asyncio.run(main())
