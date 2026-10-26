"""holds build instructions to be used in main.py"""
from dataclasses import dataclass
from evdev import ecodes as e
from act import place, path, start

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

@dataclass
class AdoraChimps:
    """adora on chimps"""
    map = [2, 3, 2]
    dif = [3, 7]

    ninja = Monk(2693, 341, NINJA)
    et = Monk(2898, 356, HERO)
    druid = Monk(2821, 454, DRUID)
    boom = Monk(2822, 335, BOOM)

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
        [37800, path, druid, PTH3],
        [43200, path, ninja, PTH3]
    ]
