import epaper
import sys
import os

from PIL import Image, ImageDraw, ImageFont

import time

fontsdir = "/usr/local/share/fonts"

epd = epaper.epaper('epd2in13b_V4').EPD()
epd.init()
epd.Clear()

time.sleep(1)

font20 = ImageFont.truetype(os.path.join(fontsdir, 'roboto.ttf'), 20)
font10 = ImageFont.truetype(os.path.join(fontsdir, 'roboto.ttf'), 10)

blackbg = Image.new('1',(epd.height, epd.width), 255)
drawblack = ImageDraw.Draw(blackbg)
drawblack.text((10,0), 'Hi Elli,', font = font20, fill = 0)
drawblack.text((10,20), 'ja lass morgen ins Gym', font = font20, fill = 0)
drawblack.text((10,40), ':) ^^', font = font20, fill = 0)
drawblack.text((10,70), '8==============D', font = font10, fill = 0)

# IDK needed second param ..
redbg = Image.new('1', (epd.height, epd.width), 255)
drawred = ImageDraw.Draw(redbg)
# drawred.text((10,90), 'Was passiert hier??', font = font10, fill = 0)
# drawred.rectangle((0,0,0,0), fill= 0)

epd.display(epd.getbuffer(blackbg), epd.getbuffer(redbg))
