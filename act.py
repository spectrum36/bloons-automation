"""fuck you nk"""
import time
import subprocess
import io
from dataclasses import dataclass
import numpy as np

from PIL import Image, ImageOps
from wayland_automation import Mouse, Keyboard
from evdev import UInput, ecodes as e
import pytesseract as ts

ui = UInput()
mouse = Mouse(5760, 1200)
kb = Keyboard()
STEP = .3

@dataclass
class Clear:
    """clear coords"""
    x: int
    y: int

CLR = Clear(2740, 900)

def select(z):
    """here so I don't have to keep typing this"""
    mouse.click(z.x, z.y, "left")
    time.sleep(STEP)

def target(x, tgt):
    """change targeting"""
    select(x)
    time.sleep(STEP)

    if x.tgt == tgt:
        return
    change = abs(x.tgt - tgt)

    if x.tgt > tgt:
        for _ in range(change):
            ui.write(e.EV_KEY, e.KEY_TAB, 1)
            ui.syn()
            time.sleep(0.1)
            ui.write(e.EV_KEY, e.KEY_TAB, 0)
            ui.syn()
            time.sleep(0.1)
    else:
        for _ in range(change):
            ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)
            ui.syn()
            #time.sleep(0.1)
            ui.write(e.EV_KEY, e.KEY_TAB, 1)
            ui.syn()
            time.sleep(0.1)
            ui.write(e.EV_KEY, e.KEY_TAB, 0)
            ui.syn()
            ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)
            ui.syn()
            time.sleep(0.1)

    x.tgt = tgt
    select(CLR)
    time.sleep(STEP)

def cash():
    """gets cash, returns string"""
    png = subprocess.run(
        [ "grim", "-g", "2286,9 220x60", "-t", "png", "-"],
        capture_output=True, check=True,
    ).stdout

    img = Image.open(io.BytesIO(png))
    img = ImageOps.grayscale(img)
    img = img.point(lambda p: 255 if p == 255 else 0)
    img = ImageOps.invert(img)

    img.save("debug.png")

    text = ts.image_to_data(
        img,
        config="--psm 7 -c tessedit_char_whitelist=0123456789,",
        output_type=ts.Output.DICT
    )
    return text

def get_cash():
    """try to get cash"""
    while True:
        data = cash()
        for i in range(len(data['text'])):
            num = data['text'][i]
            x = data['conf'][i]
            if x != 0 and num.strip():
                num = num.replace(",", "")
                break

        try:
            c = int(num)
            return c, x
        except ValueError:
            print("int conversion failed")

def wait_cash(x):
    """wait for cash amount"""
    if x == 0:
        return
    c, conf = get_cash()
    while True:
        c, conf = get_cash()
        print(f"{c} | {conf}")
        if conf > 85:
            if x < c:
                break
        else:
            print(f"ignored cash, reading at {c}, confidence {conf}")
        time.sleep(1)

def pixel(x,y):
    """gets color of pixel"""
    penis = subprocess.run(
        ["grim", "-g", f"{x},{y} 1x1", "-t", "ppm", "-"],
        capture_output=True, check=True,
    ).stdout
    balls = tuple(penis[-3:])
    ret = []
    for i in range(3):
        ret.append(balls[i])
    return ret

def place(z):
    """places monkey"""
    mouse.click(z.x, z.y)
    time.sleep(STEP)

    ui.write(e.EV_KEY, z.key, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, z.key, 0)
    ui.syn()
    time.sleep(STEP)

    mouse.click(z.x, z.y, "left")
    time.sleep(STEP)


def start(x = 2):
    """starts the game, variable is for apopolypse, set to 1 to only hit space once for ff"""
    for _ in range(x):
        ui.write(e.EV_KEY, e.KEY_SPACE, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SPACE, 0)
        ui.syn()
        time.sleep(STEP)

def path(x, y, z=1):
    """ugprade path, z is repetition for deflation"""
    select(x)
    for _ in range(z):
        ui.write(e.EV_KEY, y, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, y, 0)
        ui.syn()
        time.sleep(STEP)
    select(CLR)
