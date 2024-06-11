import os

os.system("mkdir   mass_spring")
os.system("mkdir   mass_spring/initial4")
os.system("mkdir   mass_spring/final4")
os.system("python3 diffBespokeMorpho/mass_spring_bodyChange.py 4 train 50")
