import subprocess

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
print(pixel(2785, 675))
