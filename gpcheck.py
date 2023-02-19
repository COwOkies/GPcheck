import os
import subprocess
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.joystick
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mycontroller = config.get('values','mycontroller')


print(f"mycontroller = '{mycontroller}'")
controllers = ['mycontroller2', 'mycontroller3', 'mycontroller4']

for controller in controllers:
    try:
        value = config.get('values', controller)
        exec(f"{controller} = '{value}'")
        print(f"{controller} = '{value}'")
    except configparser.NoOptionError:
        exec(f"{controller} = None")
        print(f"{controller} = None")
        
exe_path = config.get('values','exe_path')
close = config.getboolean('values','close')

pygame.joystick.init()
controller_list = []
count = pygame.joystick.get_count()
c_name = "controller"
if count>1:
    c_name+="s"
print(f"\n{count} {c_name} found.\n————————————————————————")

if count > 0:
    for i in range(count):
        joystick = pygame.joystick.Joystick(i).get_name()
        print("->",joystick)
        controller_list.append(joystick)
    print("————————————————————————")

if mycontroller in controller_list or mycontroller2 in controller_list or mycontroller3 in controller_list or mycontroller4 in controller_list or (mycontroller.lower() == "any" and count>0):
    print(f"{mycontroller} found in Controller List of {count} {c_name}")
    print(f"Openning {exe_path}")
    subprocess.Popen(exe_path)
    
else:
    print(f"Your controller '{mycontroller}' haven't been found, you may have entered a wrong controller name.")
    print("You may need to copy the name from the currently detected controller list above.")
if close:exit()
input("")
