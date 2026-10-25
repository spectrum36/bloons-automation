import sys
from wayland_automation import Mouse
mouse = Mouse()

mouse.click(int(sys.argv[1]), int(sys.argv[2]), "nothing")
