"""
def wait_cash(c, y):
    while True:
        print(f"{c} | {y}")
        if abs((c - y)) / ((y + c) /2) < .4:
            if x < c:
                break
        else:
            print(f"ignored cash, reading at {c}")
        y = c
    return y
"""
c = 91
y = 9205

x = (c - y) / ((y + c) / 2)
print(x)
