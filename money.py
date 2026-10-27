"""fuck you nk"""
import time
import subprocess
import io
import numpy as np

from PIL import Image, ImageOps
import pytesseract as ts
import cv2 as cv

def cash():
    """gets cash, returns string"""
    png = subprocess.run(
        [ "grim", "-g", "2286,9 220x60", "-t", "png", "-"],
        capture_output=True, check=True,
    ).stdout 

    img = Image.open(io.BytesIO(png))
    img = ImageOps.grayscale(img)
    img = img.point(lambda p: 255 if p == 255 else 0)
    img = ImageOps.invert(img)
 
    text = ts.image_to_data(
        img,
        config="--psm 7 -c tessedit_char_whitelist=0123456789,",
        output_type=ts.Output.DICT
    )
    return text

last = 850
while True:
    data = cash()

    for i in range(len(data['text'])):
        conf = int(data['conf'][i])
        num = data['text'][i]
        if conf != -1 and num.strip():
            num = num.replace(",", "")
            c = conf
            break
           
    num = int(num)
    if (num - last) / ((num + last) / 2) > .4:
        print(f"{int(num)}, confidence {c}, HIGH VARIANCE")
    elif c < 90:
        print(f"{int(num)}, confidence {c}, LOW CONFIDENCE")
    else:
        print(f"{int(num)}, confidence {c}")

    last = num

    time.sleep(3)
