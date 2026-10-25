"""fuck you nk"""
import subprocess, io
from PIL import Image, ImageOps
import pytesseract as ts

def cash():
    """gets cash, returns string"""
    png = subprocess.run(
        [ "grim", "-g", "2286,9 220x60", "-t", "png", "-"],
        capture_output=True, check=True,
    ).stdout
    img = Image.open(io.BytesIO(png))

    img = ImageOps.grayscale(img)
    text = ts.image_to_string(
        img,
        config="--psm 7 -c tessedit_char_whitelist=0123456789",
    )
    print(text[:-1])
    return text
cash()
cash()
cash()
