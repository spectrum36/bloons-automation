
#Bloons TD6 Automation

This is a python script made to automate bloons td6 on linux under a wayland session. I made it so that I can cheese collection events.

It uses a very slightly modified version of wayland_automation that is stored in .venv.

##How it works

The script executes a list of build instructions stored in a class in mnk.py. Build instructions are alist of lists stored as build in each class. An instruction looks like [cash, function, monkey, *args]. 

It uses OCR to read the cash value then waits for cash to be greater than the cash value in the build instruction before executing the function, it uses argument unpacking to give the args to the specificed function, so anything after monkey will be passed to the specified function.

##How to automate a map

Map/difficulty combinations are stored as dataclasses in mnk.py. To add your own, make a new dataclass with the following variables

1. map, maps are stored as a list, given as [type, page, map number on page]. For example, adora's temple is [2, 3, 2] for [medium, page 2, map 2].

2. dif, difficulties are also stored as a list, given as [difficulty, mode]. For example, half cash is [3, 4] for [hard, half cash].

3. monkies, there isn't one variable for monkies, rather monkies are stored as instances of the Monk class. To add a ninja to your class, you would add ninja = Monk(x pos, y pos, NINJA). There's a list of constants that map each monkey to its respective hotkey. Desperado, Mermonkey, and Skywarden don't have hotkeys because they aren't assigned by default. I need to figure out a good way to handle this.

4. build, this is a list of lists, each entry is an instruction to follow. The available instructions are place (places monkey at it's x,y pos), path (upgrades a path on a monkey, PTH1-3 hold the hotkey for pathing), target (changes monkey's targeting, monkies start at 0 for first, pass the number for targeting to change to), and start (starts the game, pass 1 to start on apopolypse)

Drop a pr or something if you want me to add your build instructions to the repo.

##Variables to change

In act.py there are two things you should change to match your setup. MON is the monitor number (starting on 0) where your bloons game is, this is used to set the x position of clicks/screen reading. The Mouse class from wayland automation takes in (width, height) so that it can click on other monitors, set it to the height of your tallest monitor and width of your setup (monitor number * 1920).

In main.py, there are two variables at the top of the file. MP holds the map class to use for the run of the script. LOOP is whether or not to loop the script infinitely.
