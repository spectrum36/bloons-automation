"""fuck you nk"""
import time
import mnk
from act import mouse, STEP, wait_cash, pixel, mon_x

LOOP = False

#map to use
MP = mnk.ThreeMinesChimps

#TODO add difficulty checks
def sel_dif(dif):
    """select difficulty from list [difficulty, type]"""
    x0 = mon_x(630)
    y0 = 400
    dx0 = 330

    x1 = mon_x(940)
    y1 = 450
    dx1 = 310
    dy1 = 300

    mouse.click(x0 + (((dif[0] - 1) % 3) * dx0), y0, "left")
    time.sleep(STEP)
    if dif[1] == 1:
        mouse.click(mon_x(630), 600, "left")
        time.sleep(STEP)
    else:
        mouse.click(x1 + (((dif[1] - 2) % 3) * dx1), y1 + (((dif[1] - 2) // 3) * dy1), "left")
        time.sleep(STEP)

#TODO add map checks
def sel_map(x, dif):
    """select map from given list [type, page, map num], starting at home screen"""
    mouse.click(mon_x(950), 940, "left")
    time.sleep(STEP)

    x0 = mon_x(580)
    y0 = 970
    dx0 = 250

    x1 = mon_x(480)
    y1 = 250
    dx1 = 400
    dy1 = 400

    #select map
    if x[0] == 1:
        num = x[1] - 1
        if num == 0:
            time.sleep(STEP)
    else:
        num = x[1]

    for _ in range(num):
        mouse.click(x0 + (((x[0] - 1) % 4) * dx0), y0, "left")
        time.sleep(STEP)

    mouse.click(x1 + (((x[2] - 1) % 3) * dx1), y1 + ((x[2] // 3) * dy1), "left")
    time.sleep(STEP)

    #select difficulty
    sel_dif(dif)
    time.sleep(STEP)

    #check if save game exists
    px = pixel(mon_x(600), 500)
    if px[0] == 95 and px[1] == 148 and px[2] == 215:
        mouse.click(mon_x(1060), 720, "left")
        time.sleep(1)

    mouse.click(mon_x(80), 100, "nothing")
    time.sleep(1)

    #wait for map to load, end after selecting ok
    if (dif[0] == 3 and (dif[1] == 4 or dif[1] == 6 or dif[1] == 7)) or (dif[0] == 1 and dif[1] == 3):
        while True:
            out = pixel(mon_x(880), 750)
            print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
            if out[0] == 110 and out[1] == 231 and out[2] == 0:
                mouse.click(mon_x(880), 750, "left")
                time.sleep(1)
                mouse.click(mon_x(880), 750, "left")
                break
            time.sleep(1)
    elif dif[0] == 2 and dif[1] == 3:
        while True:
            out = pixel(mon_x(880), 750)
            print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
            if out[0] == 210 and out[1] == 210 and out[2] == 210:
                time.sleep(1)
                mouse.click(mon_x(960), 750, "left")
                break
            time.sleep(1)
    else:
        while True:
            out = pixel(mon_x(880), 750)
            print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
            if out[0] != 0 or out[1] != 0 or out[2] != 0:
                time.sleep(1)
                mouse.click(mon_x(960), 750, "left")
                break
            time.sleep(1)



def finish_chimps():
    """waits for chimps game to end and navigates end screen"""
    while True:
        px = pixel(mon_x(585), 775)
        if px[0] == 47 and px[1] == 34 and px[2] == 92:
            time.sleep(2)
            mouse.click(mon_x(585), 775, "left")
            break
        time.sleep(3)

    while True:
        px = pixel(mon_x(880), 900)
        if px[0] == 107 and px[1] == 230 and px[2] == 0:
            time.sleep(2)
            mouse.click(mon_x(880), 900, "left")
            break
        time.sleep(3)
    time.sleep(1)
    mouse.click(mon_x(680), 800, "left")
    time.sleep(1)
    while True:
        out = pixel(mon_x(880), 750)
        print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
        if out[0] != 0 or out[1] != 0 or out[2] != 0:
            mouse.click(mon_x(880), 750, "left")
            break
        time.sleep(1)

def finish():
    """waits for non-chimps game to end and navigates end screen"""
    while True:
        px = pixel(mon_x(880), 900)
        if px[0] == 107 and px[1] == 230 and px[2] == 0:
            time.sleep(2)
            mouse.click(mon_x(880), 900, "left")
            break
        time.sleep(3)
    time.sleep(1)
    mouse.click(mon_x(680), 800, "left")
    time.sleep(1)
    while True:
        out = pixel(mon_x(880), 750)
        print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
        if out[0] != 0 or out[1] != 0 or out[2] != 0:
            mouse.click(mon_x(880), 750, "left")
            break
        time.sleep(1)

def collect():
    """gets collection rewards, if present"""
    col = pixel(mon_x(865), 675)
    if col[0] != 104 or col[1] != 229 or col[2] != 0:
        return
    mouse.click(mon_x(865), 675, "left")
    time.sleep(2)

    y = 560
    x = 2000
    for i in range(18):
        tx = x + (i * 100)
        col = pixel(tx, y)
        if col[0] != 18 or col[1] != 20 or col[2] != 23:
            time.sleep(STEP)
            mouse.click(tx, y - 60, "left")
            time.sleep(1.5)
            mouse.click(tx, y - 60, "left")
            time.sleep(STEP)
    time.sleep(1)
    mouse.click(mon_x(923), 993, "left")
    time.sleep(STEP)
    mouse.click(mon_x(71), 59, "left")
    time.sleep(STEP)

def main():
    """fuck you nk, I'm automating chimps"""
    sel_map(MP.map, MP.dif)
    time.sleep(2)

    #build instruction loop
    for i in MP.build:
        cash, instruction, *args = i
        wait_cash(cash)
        instruction(*args)

    if MP.dif[0] == 3 and MP.dif[1] == 7:
        finish_chimps()
    else:
        finish()
    time.sleep(1)
    collect()
    time.sleep(1)

if LOOP:
    while True:
        main()
else:
    main()
