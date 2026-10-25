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
    #img = ImageOps.invert(img)
    img = img.point(lambda p: 255 if p == 255 else 0)

    img.save("debug.png")

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
    return c


def wait_cash(x):
    """wait for cash amount"""
    c = get_cash()
    i = 0
    while int(c) < x:
        time.sleep(3)
        c = get_cash()
        if i % 1 == 0:
            print(c)
        i = i + 1

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

def main():
    """fuck you nk, I'm automating chimps"""
    sel_map()
    time.sleep(5)
    place(NINJA)

    time.sleep(STEP)
    start()

    wait_cash(325)
    path(PTH3, NINJA)

    wait_cash(700)
    place(ET)

    wait_cash(485)
    path(PTH3, NINJA)

    for _ in range(2):
        wait_cash(380)
        path(PTH1, NINJA)

    wait_cash(2430)
    path(PTH3, NINJA)

    wait_cash(430)
    place(ICE)
    select(CLR)

    wait_cash(430)
    place(DRUID)
    select(CLR)

    wait_cash(380)
    path(PTH1, DRUID)

    wait_cash(270)
    path(PTH2, DRUID)

    wait_cash(380)
    path(PTH2, DRUID)

    wait_cash(1135)
    path(PTH2, DRUID)

    wait_cash(5400)
    path(PTH3, NINJA)

    wait_cash(920)
    path(PTH1, DRUID)

    wait_cash(5290)
    path(PTH2, DRUID)

    wait_cash(160)
    path(PTH1, ICE)

    wait_cash(160)
    path(PTH3, ICE)

    wait_cash(215)
    path(PTH3, ICE)

    wait_cash(2050)
    path(PTH3, ICE)

    wait_cash(2970)
    path(PTH3, ICE)

    wait_cash(32400)
    path(PTH3, ICE)

    wait_cash(270)
    place(WIZ)
    select(CLR)

    wait_cash(190)
    path(PTH1, WIZ)

    for _ in range(2):
        wait_cash(325)
        path(PTH3, WIZ)

    wait_cash(485)
    path(PTH1, WIZ)

    wait_cash(1620)
    path(PTH3, WIZ)

    wait_cash(3025)
    path(PTH3, WIZ)

    wait_cash(28620)
    path(PTH3, WIZ)

    wait_cash(43200)
    path(PTH3, NINJA)

    while True:
        px = pixel(2505, 775)
        if px[0] == 47 and px[1] == 34 and px[2] == 92:
            mouse.click(2505, 775, "left")
            break
        time.sleep(3)

main()
