import epaper
import sys
import os
import time
from PIL import Image, ImageDraw, ImageFont
import socket
from datetime import datetime


def draw(text):
    w_img = Image.new('1', (epd.height, epd.width), 255)
    w_draw = ImageDraw.Draw(w_img)
    w_draw.text((10, 0), text, font=font20, fill=0)

    # IDK needed second param ..
    r_img = Image.new('1', (epd.height, epd.width), 255)
    r_draw = ImageDraw.Draw(r_img)

    epd.display(epd.getbuffer(w_img), epd.getbuffer(r_img))
    log("draw", text)


def log(function_name, text):
    with open("log.txt", "a") as myfile:
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        myfile.write(f"{date} {function_name} -> {text}\n")

log("main", "Started :)")


fonts_dir = "/usr/local/share/fonts"
font20 = ImageFont.truetype(os.path.join(fonts_dir, 'roboto.ttf'), 20)
font10 = ImageFont.truetype(os.path.join(fonts_dir, 'roboto.ttf'), 10)

epd = epaper.epaper('epd2in13b_V4').EPD()
epd.init()
log("main", "epd inited")
epd.Clear()
log("main", "epd clear")

draw("Initialized")

port = 8089
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', port))
serversocket.listen(1)
log("main", f"Listen on {8089}")


draw(f"Listening on Port {port}")

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(1024)
    if len(buf) > 0:
        text = str(buf, 'UTF-8')
        draw(text)
