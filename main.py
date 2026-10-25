"""fuck you nk"""
import time
import subprocess
from wayland_automation import Mouse, Keyboard
from evdev import UInput, ecodes as e
ui = UInput()
mouse = Mouse()
kb = Keyboard()
STEP = .3

WIZ = [2690, 565, e.KEY_A]
NINJA = [2693, 337, e.KEY_D]
ET = [2822, 337, e.KEY_U]
DRUID = [2822, 457, e.KEY_G]
ICE = [2693, 457, e.KEY_T]

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

def place(x, y, key):
    """places wizard"""
    mouse.click(x, y)
    time.sleep(STEP)

    ui.write(e.EV_KEY, key, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, key, 0)
    ui.syn()
    time.sleep(STEP)

    mouse.click(x, y, "left")

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

def path1():
    """ugprade path 1"""
    ui.write(e.EV_KEY, e.KEY_COMMA, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_COMMA, 0)
    ui.syn()
    time.sleep(0.1)

def path2():
    """upgrade path 2"""
    ui.write(e.EV_KEY, e.KEY_DOT, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_DOT, 0)
    ui.syn()
    time.sleep(0.1)

def path3():
    """upgrade path 3"""
    ui.write(e.EV_KEY, e.KEY_SLASH, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_SLASH, 0)
    ui.syn()
    time.sleep(0.1)

def clr_screen():
    """clicks to clear screen of sidebar"""
    mouse.click(2220, 250, "left")

def main():
    """fuck you nk, I'm automating chimps"""
    #sel_map()
    time.sleep(5)
    place(NINJA[0], NINJA[1], NINJA[2])
    place(ET[0], ET[1], ET[2])
    place(ICE[0], ICE[1], ICE[2])
    place(DRUID[0], DRUID[1], DRUID[2])
    place(WIZ[0], WIZ[1], WIZ[2])

main()
