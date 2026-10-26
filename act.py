"""fuck you nk"""
import time
import subprocess
import io
from dataclasses import dataclass

from PIL import Image, ImageOps
from wayland_automation import Mouse, Keyboard
from evdev import UInput, ecodes as e
import pytesseract as ts
ui = UInput()
mouse = Mouse()
kb = Keyboard()
STEP = .3

TGT = e.KEY_TAB

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

    #img.save("debug.png")

    text = ts.image_to_string(
        img,
        config="--psm 7 -c tessedit_char_whitelist=0123456789",
    )
    return text

def get_cash():
    """try to get cash"""
    c = ""
    while c == "":
        c = cash()[:-1]
        try:
            int(c)
        except ValueError:
            c = ""
    return int(c)


def wait_cash(x, y):
    """wait for cash amount"""
    c = get_cash()
    while True:
        c = get_cash()
        print(f"{c} | {y}")
        if (c - y) / ((y + c) /2) < .4:
            if x < c:
                break
            time.sleep(1)
        else:
            print(f"ignored cash, reading at {c}")
        y = c
    return y

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
    return get_cash()

def start():
    """starts the game"""
    for _ in range(2):
        ui.write(e.EV_KEY, e.KEY_SPACE, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SPACE, 0)
        ui.syn()
        time.sleep(STEP)
    return get_cash()

def path(x, y):
    """ugprade path"""
    select(x)
    ui.write(e.EV_KEY, y, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, y, 0)
    ui.syn()
    time.sleep(STEP)
    select(CLR)
    return get_cash()
