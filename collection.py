import time
import subprocess
from wayland_automation import Mouse, Keyboard
mouse = Mouse()
kb = Keyboard()
step = 0.3

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



# 18 20 23
y = 560
x = 2000
for i in range(18):
    tx = x + (i * 100)
    col = pixel(tx, y)
    if col[0] != 18 or col[1] != 20 or col[2] != 23:
        time.sleep(step)
        mouse.click(tx, y - 60, "left")
        time.sleep(1)
        mouse.click(tx, y - 60, "left")
        time.sleep(step)
    
