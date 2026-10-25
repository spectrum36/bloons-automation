"""fuck you nk"""
import time
import subprocess
import io
from PIL import Image, ImageOps
from wayland_automation import Mouse, Keyboard
from evdev import UInput, ecodes as e
import pytesseract as ts
ui = UInput()
mouse = Mouse()
kb = Keyboard()
STEP = .3

WIZ = [2690, 565, e.KEY_A]
NINJA = [2693, 337, e.KEY_D]
ET = [2822, 337, e.KEY_U]
DRUID = [2822, 457, e.KEY_G]
ICE = [2693, 457, e.KEY_T]
CLR = [2740, 1000]
PTH1 = e.KEY_COMMA
PTH2 = e.KEY_DOT
PTH3 = e.KEY_SLASH

def select(x):
    """here so I don't have to keep typing this"""
    mouse.click(x[0], x[1], "left")
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
        time.sleep(3)
        c = get_cash()
        print(f"{c} | {y}")
        if (c - y) / ((y + c) /2) < .4:
            if x < c:
                break
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

def place(x):
    """places wizard"""
    mouse.click(x[0], x[1])
    time.sleep(STEP)

    ui.write(e.EV_KEY, x[2], 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, x[2], 0)
    ui.syn()
    time.sleep(STEP)

    mouse.click(x[0], x[1], "left")
    time.sleep(STEP)
    return get_cash()

def sel_map():
    """from home screen, selects adora's temple on chimps"""
    mouse.click(2874, 931, "left")
    time.sleep(STEP)

    #navigate to page 3 intemediate
    mouse.click(2734, 931, "left")
    time.sleep(STEP)
    mouse.click(2734, 931, "left")
    time.sleep(STEP)
    mouse.click(2734, 931, "left")
    time.sleep(STEP)

    #select adora's temple
    mouse.click(2880, 270, "left")
    time.sleep(STEP)

    #select chimps
    mouse.click(3200, 400, "left")
    time.sleep(STEP)
    mouse.click(3530, 730, "left")
    time.sleep(STEP)

    #wait for map to load, end after selecting ok
    while True:
        out = pixel(2800, 750)
        print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
        if out[0] == 110 and out[1] == 231 and out[2] == 0:
            mouse.click(2800, 750, "left")
            break
        time.sleep(1)

def start():
    """starts the game"""
    for _ in range(2):
        ui.write(e.EV_KEY, e.KEY_SPACE, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SPACE, 0)
        ui.syn()
        time.sleep(STEP)

def path(x, y):
    """ugprade path"""
    select(y)
    ui.write(e.EV_KEY, x, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, x, 0)
    ui.syn()
    time.sleep(STEP)
    select(CLR)
    return get_cash()

def main():
    """fuck you nk, I'm automating chimps"""
    sel_map()
    time.sleep(5)
    last = place(NINJA)

    time.sleep(STEP)
    start()

    last = wait_cash(325, last)
    last = path(PTH3, NINJA)

    last = wait_cash(700, last)
    last = place(ET)

    last = wait_cash(485, last)
    last = path(PTH3, NINJA)

    for _ in range(2):
        last = wait_cash(380, last)
        last = path(PTH1, NINJA)

    last = wait_cash(2430, last)
    last = path(PTH3, NINJA)

    last = wait_cash(430, last)
    last = place(ICE)
    select(CLR)

    wait_cash(430, last)
    last = place(DRUID)
    select(CLR)

    last = wait_cash(380, last)
    last = path(PTH1, DRUID)

    last = wait_cash(270, last)
    last = path(PTH2, DRUID)

    last = wait_cash(380, last)
    last = path(PTH2, DRUID)

    last = wait_cash(1135, last)
    last = path(PTH2, DRUID)

    last = wait_cash(5400, last)
    last = path(PTH3, NINJA)

    last = wait_cash(920, last)
    last = path(PTH1, DRUID)

    last = wait_cash(5290, last)
    last = path(PTH2, DRUID)

    last = wait_cash(160, last)
    last = path(PTH1, ICE)

    last = wait_cash(160, last)
    last = path(PTH3, ICE)

    last = wait_cash(215, last)
    last = path(PTH3, ICE)

    last = wait_cash(2050, last)
    last = path(PTH3, ICE)

    last = wait_cash(2970, last)
    last = path(PTH3, ICE)

    last = wait_cash(32400, last)
    last =path(PTH3, ICE)

    last = wait_cash(270, last)
    last = place(WIZ)
    select(CLR)

    last = wait_cash(190, last)
    last = path(PTH1, WIZ)

    for _ in range(2):
        last = wait_cash(325, last)
        last = path(PTH3, WIZ)

    last = wait_cash(485, last)
    last = path(PTH1, WIZ)

    last = wait_cash(1620, last)
    last = path(PTH3, WIZ)

    last = wait_cash(3025, last)
    last = path(PTH3, WIZ)

    last = wait_cash(28620, last)
    last = path(PTH3, WIZ)

    last = wait_cash(43200, last)
    last = path(PTH3, NINJA)

    while True:
        px = pixel(2505, 775)
        if px[0] == 47 and px[1] == 34 and px[2] == 92:
            mouse.click(2505, 775, "left")
            break
        time.sleep(3)

main()
