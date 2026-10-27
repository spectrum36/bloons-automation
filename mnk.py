"""holds build instructions to be used in main.py"""
from dataclasses import dataclass
from evdev import ecodes as e
from act import place, path, start, target, mon_x

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
DESP  = "ph"
DRUID = e.KEY_G
FARM  = e.KEY_H
GUN   = e.KEY_M
GLUE  = e.KEY_Y
HELI  = e.KEY_B
HERO  = e.KEY_U
ICE   = e.KEY_T
MERMK = "ph"
MORT  = e.KEY_N
NINJA = e.KEY_D
SKYWD = "ph"
SNIP  = e.KEY_Z
SPIKE = e.KEY_J
SUB   = e.KEY_X
SUPER = e.KEY_S
TACK  = e.KEY_R
VILL  = e.KEY_K
WIZ   = e.KEY_A


@dataclass
class Monk:
    """standardized monkey"""
    x: int
    y: int
    key: int
    tgt: int = 0

#set monkey x value to be as if it is on monitor 0 (value - (1920 * monitor number))
#use mon_x() to change the x value for monkies to be on the right monitor
@dataclass
class AdoraChimps:
    """adora on chimps"""
    map = [2, 3, 2]
    dif = [3, 7]

    ninja = Monk(mon_x(1043), 341, NINJA)
    et = Monk(mon_x(978), 356, HERO)
    druid = Monk(mon_x(901), 454, DRUID)
    boom = Monk(mon_x(902), 335, BOOM)
    snipe = Monk(mon_x(768), 449, SNIP)

    build = [
        [0, place, ninja],
        [0, start],
        [325, path, ninja, PTH3],
        [700, place, et],
        [380, path, ninja, PTH1],
        [380, path, ninja, PTH1],
        [485, path, ninja, PTH3],
        [2430, path, ninja, PTH3],
        [430, place, druid],
        [380, path, druid, PTH1],
        [270, path, druid, PTH2],
        [380, path, druid, PTH2],
        [920, path, druid, PTH1],
        [1135, path, druid, PTH2],
        [5400, path, ninja, PTH3],
        [5290, path, druid, PTH2],
        [240, place, boom],
        [110, path, boom, PTH3],
        [325, path, boom, PTH1],
        [300, path, boom, PTH1],
        [325, path, boom, PTH3],
        [650, path, boom, PTH1],
        [2160, path, boom, PTH1],
        [35000, path, boom, PTH1],
        [37800, path, druid, PTH2],
        [43200, path, ninja, PTH3],
        [380, place, snipe],
        [270, path, snipe, PTH2],
        [485, path, snipe, PTH2],
        [485, path, snipe, PTH3],
        [485, path, snipe, PTH3],
        [2915, path, snipe, PTH3],
        [4439, path, snipe, PTH3],
        [16090, path, snipe, PTH3]
    ]

@dataclass
class LoopDeflation:
    """loop on deflation"""
    map = [1, 1, 2]
    dif = [1, 3]

    dart = Monk(mon_x(852), 506, DART)
    build = [
        [0, place, dart],
        [0, path, dart, PTH2, 2],
        [0, path, dart, PTH3, 5],
        [0, start]
    ]
