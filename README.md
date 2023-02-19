# GPcheck
GPcheck (GamePad Checker) let you load a .exe file if a controller you choosed is plugged.

----------------------
Install requirements : (Pygame)
pip install -r requirements.txt

You can change values manually from the config.ini file.

mycontroller -> (string) The controller name you choose. You can write "any" if you want the exe to open if any controller is detected.
exe_path -> (string) Choose the .exe file you want to open here.
close -> (boolean) ose if the program should close or stay (might be useful to get your controller name)

-----------------------
When you're done, you can rename the file extension to .pyw so the python console don't open !


GamePad Checker check active controller and make a list of them.
If it finds a controller with the name you asked for it'll load the .exe path you gave him.

This program was originally intended for Playnite Fullscreen but it should works with a lot of apps :)

Made By COwOkie#6114 - Discord




