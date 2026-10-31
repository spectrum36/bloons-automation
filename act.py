"""fuck you nk"""
import time
import subprocess
import io
from dataclasses import dataclass

from PIL import Image, ImageOps
from wayland_automation import Mouse
from evdev import UInput, ecodes as e
import pytesseract as ts



#monitor number that bloons is on, starts at 0
MON = 1
def mon_x(x):
    """changes the x value to be on the right monitor"""
    return x + (1920 * MON)

ui = UInput()

#mouse class takes in (width, height)
#width is the total width of your environment (3 monitors is 1920 X 3 = 5760)
#height is the height of your tallest monitor
mouse = Mouse(5760, 1200)

STEP = .3

CASHX = mon_x(366)

@dataclass
class Clear:
    """clear coords"""
    x: int
    y: int

CLR = Clear(mon_x(820), 900)

def ability(x):
    """uses specified ability"""
    ui.write(e.EV_KEY, x, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, x, 0)
    ui.syn()
    time.sleep(STEP)

def click(x, y):
    """build instruction, clicks on specified point on screen"""
    mouse.click(x, y, "left")
    time.sleep(STEP)

def wait(x):
    """build instruction, waits specified number of seconds"""
    time.sleep(x)

def img_grab(x, y, x0, y0):
    """image grabbing and processing for ocr"""
    png = subprocess.run(
        [ "grim", "-g", f"{x},{y} {x0}x{y0}", "-t", "png", "-"],
        capture_output=True, check=True,
    ).stdout

    img = Image.open(io.BytesIO(png))
    img = ImageOps.grayscale(img)
    img = img.point(lambda p: 255 if p == 255 else 0)
    img = ImageOps.invert(img)

    return img

def rnd(dif):
    """gets round, returns dict"""
    if dif[0] == 3 and (dif[1] == 6 or dif == 7):
        img = img_grab(3300, 30, 87, 40)
    else:
        img = img_grab(3300, 30, 102, 40)
    img.save("debug.png")

    text = ts.image_to_data(
        img,
        config="--psm 7 -c tessedit_char_whitelist=0123456789/",
        output_type=ts.Output.DICT
    )
    return text


def get_round(dif):
    """validates grabbed round, returns int"""
    while True:
        data = rnd(dif)
        for i in range(len(data['text'])):
            num = data['text'][i]
            x = data['conf'][i]
            if x != 0 and num.strip():
                break
        try:
            c = int(num)
            return c, x
        except ValueError:
            print("int conversion failed")

def wait_round(x, dif):
    """waits for round number"""
    while True:
        c, conf = get_round(dif)
        print(f"{c} | {conf}")
        if conf > 85:
            if x <= c:
                break
        else:
            print(f"ignored round, reading at {c}, confidence {conf}")
        time.sleep(1)

def cash():
    """gets cash, returns dict"""
    img = img_grab(CASHX, 9, 220, 60)

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

def start(x = 2):
    """starts the game, variable is for apopolypse, set to 1 to only hit space once for ff"""
    for _ in range(x):
        ui.write(e.EV_KEY, e.KEY_SPACE, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SPACE, 0)
        ui.syn()
        time.sleep(STEP)
