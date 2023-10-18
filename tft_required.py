import board
import displayio
from adafruit_st7789 import ST7789

displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

dbus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(dbus, rotation=270, width=240, height=135, rowstart=40, colstart=53)
