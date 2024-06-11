import os

os.system("mkdir   mass_spring")
os.system("mkdir   mass_spring/initial4")
os.system("mkdir   mass_spring/final4")
os.system("python3 diffBespokeMorpho/mass_spring_bodyChange.py 4 train 0")

os.system("mkdir mass_spring/merged4")
os.system("python3 diffBespokeMorpho/mergeFrames.py")
os.system("rm -r mass_spring/initial4")
os.system("rm -r mass_spring/final4")
os.system("rm beforeAfter.mp4")
os.system("ffmpeg -i mass_spring/merged4/%d.png -c:v libx264 -pix_fmt yuv420p beforeAfter.mp4")
os.system("rm -r mass_spring/merged4")
