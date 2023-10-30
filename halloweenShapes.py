import time
import gc
import board
import displayio
import random
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon

# Constants
PUMPKIN_CENTER_X = 120
PUMPKIN_CENTER_Y = 100
PUMPKIN_RADIUS = 25
PUMPKIN_OFFSET = 7
STEM_OFFSET = 48
STEM_WIDTH = 12
STEM_HEIGHT = 24
MOON_X = 20
MOON_Y = 30
MOON_RADIUS = 10
CRESENT_OFFSET = 5
LIGHTNING = [(180, 0), (165, 40), (170, 40), (166, 60), (185, 30), (175, 30), (190, 0)]

# Colors
PUMPKIN = 0xFFAA00
BACKGROUND = 0X6600AA
MOON = 0xCCCC00
STEM = 0x00AA00
WHITE = 0xFFFFFF


displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

dbus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(dbus, rotation=270, width=240, height=135, rowstart=40, colstart=53)


# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 3)
color_palette = displayio.Palette(5)
color_palette[0] = BACKGROUND
color_palette[1] = PUMPKIN
color_palette[2] = MOON
color_palette[3] = STEM
color_palette[4] = WHITE
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)
display.show(main_group)

# Draw Pumpkin (Created from 3 circles and rectangle)
pumpkin = []
for i in range(3):
    circle = Circle(PUMPKIN_CENTER_X + ((i-1) * PUMPKIN_OFFSET), PUMPKIN_CENTER_Y, PUMPKIN_RADIUS, fill=PUMPKIN)
    pumpkin.append(circle)
for circles in pumpkin:
    main_group.append(circles)
stem = Rect(PUMPKIN_CENTER_X - int(STEM_WIDTH / 2), PUMPKIN_CENTER_Y - STEM_OFFSET, STEM_WIDTH, STEM_HEIGHT, fill=STEM)
main_group.append(stem)

# Cresent Moon
cresent = Circle(MOON_X, MOON_Y, MOON_RADIUS, fill=MOON)
main_group.append(cresent)
shadow = Circle(MOON_X - CRESENT_OFFSET, MOON_Y - CRESENT_OFFSET, MOON_RADIUS, fill=BACKGROUND)
main_group.append(shadow)

# Lightning
lightning = Polygon(LIGHTNING, outline=BACKGROUND, close=True, colors=2)
main_group.append(lightning)

count = 0
direction = 1
while True:
    val = random.randint(1, 5)
    if val == 1:
        for i in range(3):
            lightning.outline = WHITE
            time.sleep(0.1)
            lightning.outline = BACKGROUND
            time.sleep(0.05)
    time.sleep(0.5)

