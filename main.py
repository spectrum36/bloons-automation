"""fuck you nk"""
import time
import mnk
from act import mouse, STEP, wait_cash, pixel

#TODO add difficulty checks
def sel_dif(x):
    """select difficulty from list [difficulty, type]"""
    x0 = 2550
    y0 = 400
    dx0 = 330

    x1 = 2860
    y1 = 450
    dx1 = 310
    dy1 = 300

    mouse.click(x0 + (((x[0] - 1) % 3) * dx0), y0, "left")
    time.sleep(STEP)
    if x[1] == 1:
        mouse.click(2550, 600, "nothing")
        time.sleep(STEP)
    else:
        mouse.click(x1 + (((x[1] - 2) % 3) * dx1), y1 + (((x[1] - 2) // 3) * dy1), "left")
        time.sleep(STEP)

#TODO add map checks
def sel_map(x, y):
    """select map from given list [type, page, map num], starting at home screen"""
    mouse.click(2870, 940, "left")
    time.sleep(STEP)

    x0 = 2500
    y0 = 970
    dx0 = 250

    x1 = 2400
    y1 = 250
    dx1 = 400
    dy1 = 400

    #select map
    if x[0] == 1:
        num = x[1] - 1
    else:
        num = x[1]

    for _ in range(num):
        mouse.click(x0 + (((x[0] - 1) % 4) * dx0), y0, "left")
        time.sleep(STEP)

    mouse.click(x1 + (((x[2] - 1) % 3) * dx1), y1 + ((x[2] // 3) * dy1), "left")
    time.sleep(STEP)

    #select difficulty
    sel_dif(y)
    time.sleep(STEP)

    #check if save game exists
    px = pixel(2500, 500)
    if px[0] == 95 and px[1] == 148 and px[2] == 215:
        mouse.click(2980, 720, "left")
        time.sleep(1)

    #wait for map to load, end after selecting ok
    if y[0] != 2 and y[1] != 3:
        while True:
            out = pixel(2800, 750)
            print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
            if out[0] == 110 and out[1] == 231 and out[2] == 0:
                mouse.click(2800, 750, "left")
                time.sleep(1)
                mouse.click(2800, 750, "left")
                break
            time.sleep(1)
    else:
        while True:
            out = pixel(2800, 750)
            print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
            if out[0] == 210 and out[1] == 210 and out[2] == 210:
                time.sleep(1)
                mouse.click(2880, 750, "left")
                break
            time.sleep(1)

def finish_chimps():
    """waits for chimps game to end and navigates end screen"""
    while True:
        px = pixel(2505, 775)
        if px[0] == 47 and px[1] == 34 and px[2] == 92:
            time.sleep(2)
            mouse.click(2505, 775, "left")
            break
        time.sleep(3)

    while True:
        px = pixel(2800, 900)
        if px[0] == 107 and px[1] == 230 and px[2] == 0:
            time.sleep(2)
            mouse.click(2800, 900, "left")
            break
        time.sleep(3)
    time.sleep(1)
    mouse.click(2600, 800, "left")
    time.sleep(1)
    while True:
        out = pixel(2800, 750)
        print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
        if out[0] != 0 or out[1] != 0 or out[2] != 0:
            mouse.click(2800, 750, "left")
            break
        time.sleep(1)

def finish():
    """waits for non-chimps game to end and navigates end screen"""
    while True:
        px = pixel(2800, 900)
        if px[0] == 107 and px[1] == 230 and px[2] == 0:
            time.sleep(2)
            mouse.click(2800, 900, "left")
            break
        time.sleep(3)
    time.sleep(1)
    mouse.click(2600, 800, "left")
    time.sleep(1)
    while True:
        out = pixel(2800, 750)
        print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
        if out[0] != 0 or out[1] != 0 or out[2] != 0:
            mouse.click(2800, 750, "left")
            break
        time.sleep(1)

def collect():
    """gets collection rewards, if present"""
    col = pixel(2785, 675)
    if col[0] != 104 or col[1] != 229 or col[2] != 0:
        return
    mouse.click(2785, 675, "left")
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
    mouse.click(2843, 993, "left")
    time.sleep(STEP)
    mouse.click(1991, 59, "left")
    time.sleep(STEP)

def main():
    """fuck you nk, I'm automating chimps"""
    mp = mnk.LoopDeflation
    sel_map(mp.map, mp.dif)
    time.sleep(2)

    #build instruction loop
    for i in mp.build:
        cash, instruction, *args = i
        wait_cash(cash)
        instruction(*args)

    if mp.dif[0] == 3 and mp.dif[1] == 7:
        finish_chimps()
    else:
        finish()
    time.sleep(1)
    collect()
    time.sleep(1)

#runs main infinitely
while True:
    main()
