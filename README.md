
# Bloons TD6 Automation

This is a python script made to automate bloons td6 on linux under a wayland session. I made it so that I can cheese collection events.

It uses a very slightly modified version of wayland_automation, replace mouse_controller.py in your .venv with the one in the repo.

It also requires grim, tesseract, wtype, and wayland-utils. These (and the other python dependencies) are in the flake.nix for the shell.

## How it works

The script executes a list of build instructions stored in a class in mnk.py. Build instructions are alist of lists stored as build in each class. An instruction looks like [cash, function, monkey, *args]. 

It uses OCR to read the cash value then waits for cash to be greater than the cash value in the build instruction before executing the function, it uses argument unpacking to give the args to the specificed function, so anything after monkey will be passed to the specified function.

## Variables to change

In act.py there are two things you should change to match your setup. MON is the monitor number (starting on 0) where your bloons game is, this is used to set the x position of clicks/screen reading. The Mouse class from wayland automation takes in (width, height) so that it can click on other monitors, set it to the height of your tallest monitor and width of your setup (monitor number * 1920).

In main.py, there are two variables at the top of the file. MP holds the map class to use for the run of the script. LOOP is whether or not to loop the script infinitely.

## How to automate a map

Map/difficulty combinations are stored as dataclasses in mnk.py. To add your own, make a new dataclass with the following variables

1. Map, maps are stored as a list, given as [type, page, map number on page]. For example, adora's temple is [2, 3, 2] for [medium, page 2, map 2].

2. Dif, difficulties are also stored as a list, given as [difficulty, mode]. For example, half cash is [3, 4] for [hard, half cash].

3. Monkies, there isn't one variable for monkies, rather monkies are stored as instances of the Monk class. To add a ninja to your class, you would add ninja = Monk(x pos, y pos, NINJA). There's a list of constants that map each monkey to its respective hotkey. Desperado, Mermonkey, and Skywarden don't have default hotkeys, I have them set to backslash, o and p respectively, so change your hotkeys to match this if you use instructions that use those.

4. Build, this is a list of lists, each entry is an instruction to follow. The available instructions are:
    
    1. Place, places monkey at it's x,y pos 

    2. Path, upgrades a path on a monkey, PTH1-3 hold the hotkey for pathing 

    3. Target, changes monkey's targeting, monkies start at 0 for first, pass the number for targeting to change to
    
    4. Start (starts the game, pass 1 to start on apopolypse). Place, path, and target are methods in the Monk class.

    5. Wait, self explanatory, pass number of seconds to wait

    6. Click, also self explanatory, pass x,y coords to click on, used for interacting with map objects

    7. Ability, uses an ability, pass it the ecode for the ability key (e.KEY_1 for ability 1)

Place, path and target are methods in the Monk class.

Drop a pr or something if you want me to add your build instructions to the repo.

