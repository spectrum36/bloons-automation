"""holds build instructions to be used in main.py"""
import time
from dataclasses import dataclass
from evdev import ecodes as e
from act import start, mon_x, STEP, mouse, ui


PTH1 = e.KEY_COMMA
PTH2 = e.KEY_DOT
PTH3 = e.KEY_SLASH

TGT = e.KEY_TAB

ACE   = e.KEY_V
ALCH  = e.KEY_F
BEAST = e.KEY_I
BOMB  = e.KEY_E
BOOM  = e.KEY_W
BUCC  = e.KEY_C
DART  = e.KEY_Q
DESP  = e.KEY_BACKSLASH
DRUID = e.KEY_G
FARM  = e.KEY_H
GUN   = e.KEY_M
GLUE  = e.KEY_Y
HELI  = e.KEY_B
HERO  = e.KEY_U
ICE   = e.KEY_T
MERMK = e.KEY_O
MORT  = e.KEY_N
NINJA = e.KEY_D
SKYWD = e.KEY_P
SNIP  = e.KEY_Z
SPIKE = e.KEY_J
SUB   = e.KEY_X
SUPER = e.KEY_S
TACK  = e.KEY_R
VILL  = e.KEY_K
WIZ   = e.KEY_A


class Monk:
    """standardized monkey"""
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key
        self.tgt = 0

    def clear(self):
        """clears sidebar"""
        mouse.click(mon_x(820), 900, "left")

    def select(self):
        """here so I don't have to keep typing this"""
        mouse.click(self.x, self.y, "left")
        time.sleep(STEP)

    def target(self, z):
        """change targeting"""
        self.select()
        time.sleep(STEP)

        if self.tgt == z:
            return
        change = abs(self.tgt - z)

        if self.tgt > z:
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

        self.tgt = z
        self.clear()
        time.sleep(STEP)

    def place(self):
        """places monkey"""
        mouse.click(self.x, self.y)
        time.sleep(STEP)

        ui.write(e.EV_KEY, self.key, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, self.key, 0)
        ui.syn()
        time.sleep(STEP)

        mouse.click(self.x, self.y, "left")
        time.sleep(STEP)

    def path(self, pth, z=1):
        """ugprade path, z is repetition for deflation"""
        self.select()
        for _ in range(z):
            ui.write(e.EV_KEY, pth, 1)
            ui.syn()
            time.sleep(0.1)
            ui.write(e.EV_KEY, pth, 0)
            ui.syn()
            time.sleep(STEP)
        self.clear()

#set monkey x value to be as if it is on monitor 0 (value - (1920 * monitor number))
#use mon_x() to change the x value for monkies to be on the right monitor
@dataclass
class AdoraChimps:
    """adora on chimps"""
    map = [2, 3, 2]
    dif = [3, 7]

    ninja = Monk(mon_x(768), 341, NINJA)
    et = Monk(mon_x(978), 356, HERO)
    druid = Monk(mon_x(901), 454, DRUID)
    boom = Monk(mon_x(902), 335, BOOM)
    snipe = Monk(mon_x(768), 449, SNIP)

    build = [
        [0, ninja.place],
        [0, start],
        [325, ninja.path, PTH3],
        [700, et.place],
        [380, ninja.path, PTH1],
        [380, ninja.path, PTH1],
        [485, ninja.path, PTH3],
        [2430, ninja.path, PTH3],
        [430, druid.place],
        [380, druid.path, PTH1],
        [270, druid.path, PTH2],
        [380, druid.path, PTH2],
        [920, druid.path, PTH1],
        [1135, druid.path, PTH2],
        [5400, ninja.path, PTH3],
        [5290, druid.path, PTH2],
        [240, boom.place],
        [110, boom.path, PTH3],
        [325, boom.path, PTH1],
        [300, boom.path, PTH1],
        [325, boom.path, PTH3],
        [650, boom.path, PTH1],
        [2160, boom.path, PTH1],
        [35000, boom.path, PTH1],
        [37800, druid.path, PTH2],
        [43200, ninja.path, PTH3],
        [380, snipe.path],
        [270, snipe.path, PTH2],
        [485, snipe.path, PTH2],
        [485, snipe.path, PTH3],
        [485, snipe.path, PTH3],
        [2915, snipe.path, PTH3],
        [4439, snipe.path, PTH3],
        [16090, snipe.path, PTH3]
    ]

@dataclass
class LoopDeflation:
    """loop on deflation"""
    map = [1, 1, 2]
    dif = [1, 3]

    dart = Monk(mon_x(852), 506, DART)
    build = [
        [0, dart.place],
        [0, dart.path, PTH2, 2],
        [0, dart.path, PTH3, 5],
        [0, start]
    ]
