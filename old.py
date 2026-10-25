import time
import subprocess
from wayland_automation import Mouse, Keyboard
from evdev import UInput, ecodes as e
ui = UInput()
mouse = Mouse()
kb = Keyboard()
step = .3
#x, y = gui.position()

#play x 4813, y 962, click 1

#expert x 5157, y 972, click 2

#muddy x 5249, y 617, click 1

#easy x 4472, y 416, click 1

#delfation x 5080, y 445
def pixel(x,y):
    penis = subprocess.run(
        ["grim", "-g", f"{x},{y} 1x1", "-t", "ppm", "-"],
        capture_output=True, check=True,
    ).stdout
    return tuple(penis[-3:])
    ret = []
    for i in range(3):
        ret[i] = int(penis[i])
    return ret

def main():
    mouse.click(2874, 931, "left")
    time.sleep(step)

    mouse.click(3239, 931, "left")
    time.sleep(step)

    mouse.click(3239, 931, "left")
    time.sleep(step)

    mouse.click(3305, 618, "left")
    time.sleep(step)

    mouse.click(2598, 393, "left")
    time.sleep(step)

    mouse.click(3212, 484, "left")
    time.sleep(step)
    while True:
        out = pixel(2811, 761)
        print(f"{int(out[0])} | {int(out[1])} | {int(out[2])}")
        if out[0] == 93 and out[1] == 225 and out[2] == 0:
            mouse.click(2811, 701, "left")
            break
        time.sleep(1)
    #sniper   z
    #alc      f
    #villiage k
    #pth 1    ,
    #pth 2    .
    #pth 3    /

    #move to villiage pos
    time.sleep(1)
    mouse.click(2414, 486, "nothing")
    time.sleep(step)

    #place villiage
    ui.write(e.EV_KEY, e.KEY_K, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_K, 0)
    ui.syn()
    time.sleep(step)
    mouse.click(2414, 486, "left")
    time.sleep(step)

    #upgrade villiage
    mouse.click(2414, 486, "left")
    time.sleep(step)
    for _ in range(2):
        ui.write(e.EV_KEY, e.KEY_COMMA, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_COMMA, 0)
        ui.syn()
        time.sleep(0.1)

        ui.write(e.EV_KEY, e.KEY_SLASH, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SLASH, 0)
        ui.syn()
        time.sleep(0.1)

    #alch
    mouse.click(2408, 560, "nothing")

    ui.write(e.EV_KEY, e.KEY_F, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_F, 0)
    ui.syn()

    time.sleep(step)
    mouse.click(2408, 560, "left")
    time.sleep(step)

    mouse.click(2408, 560, "left")
    time.sleep(step)
    for _ in range(2):
        for _ in range(2):
            ui.write(e.EV_KEY, e.KEY_COMMA, 1)
            ui.syn()
            time.sleep(0.1)
            ui.write(e.EV_KEY, e.KEY_COMMA, 0)
            ui.syn()
            time.sleep(0.1)

        ui.write(e.EV_KEY, e.KEY_DOT, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_DOT, 0)
        ui.syn()
        time.sleep(0.1)

    #sniper 1
    mouse.click(2300, 544, "nothing")

    ui.write(e.EV_KEY, e.KEY_Z, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_Z, 0)
    ui.syn()

    time.sleep(step)
    mouse.click(2300, 544, "left")
    time.sleep(step)

    mouse.click(2300, 544, "left")
    time.sleep(step)
    for _ in range(2):
        for _ in range(2):
            ui.write(e.EV_KEY, e.KEY_SLASH, 1)
            ui.syn()
            time.sleep(0.1)
            ui.write(e.EV_KEY, e.KEY_SLASH, 0)
            ui.syn()
            time.sleep(0.1)

        ui.write(e.EV_KEY, e.KEY_DOT, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_DOT, 0)
        ui.syn()
        time.sleep(0.1)

    #sniper 1
    mouse.click(2393, 323, "nothing")

    ui.write(e.EV_KEY, e.KEY_Z, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_Z, 0)
    ui.syn()

    time.sleep(step)
    mouse.click(2393, 323, "left")
    time.sleep(step)

    mouse.click(2393, 323, "left")
    time.sleep(step)
    for _ in range(2):
        for _ in range(2):
            ui.write(e.EV_KEY, e.KEY_COMMA, 1)
            ui.syn()
            time.sleep(0.1)
            ui.write(e.EV_KEY, e.KEY_COMMA, 0)
            ui.syn()
            time.sleep(0.1)

        ui.write(e.EV_KEY, e.KEY_SLASH, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SLASH, 0)
        ui.syn()
        time.sleep(0.1)
    mouse.click(2760, 460, "left")
    time.sleep(step)
    for _ in range(2):
        ui.write(e.EV_KEY, e.KEY_SPACE, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(e.EV_KEY, e.KEY_SPACE, 0)
        ui.syn()
        time.sleep(0.1)    
    
    ui.close()

    while True:
        out = pixel(2800, 900)
        if out[0] == 107 and out[1] == 230 and out[2] == 0:
            mouse.click(2800, 840, "left")
            time.sleep(2)
            mouse.click(2630, 820, "left")
            break
        time.sleep(1)
    time.sleep(1)
    while True:
        out = pixel(2811, 761)
        if out[0] == 0 and out[1] == 0 and out[2] == 0:
            time.sleep(1)
        else:
            break
    out = pixel(2783, 675)
    if out[0] != 104 and out[1] != 209 and out[2] != 0:
        return
    
    time.sleep(step)
    mouse.click(2783, 615)
    time.sleep(step)
    

main()
