# Sorting Algorithm Visualiser
Sorting algorithm visualiser like the ones you see on youtube.
Written in python in an hour.. will work on cleaning it up a bit.
Program is NOT designed to be efficient at sorting, more it is for understanding how different sorting algorithms work.


# Demo
<img src="https://raw.githubusercontent.com/r333mo/algorithm_visualiser/main/demo.gif">

# Running
Have python installed.
<br>
Might also need pygame module: `pip install pygame`
<br>
Run with: `python3 algorithm_visualiser.py` (or py, python etc)
<br>
Use ESC or Q to exit- note that this won't work during sorting (but you can always CTRL+C terminal).
<br>
Use R to reset and scramble list.
<br>
Use SPACE to run sorting algorithm (currently only bubble sort, will add actual good algorithms at some point)
<br>
Program can take arguments when called from command line:
    <br>```--debug```: prints out some debug messages, as well as array on each iteration.
    <br>```-wX```: width of blocks, where X is width (eg -w10 for 10px wide blocks)
    <br>```-fpsX```: fps to run at, where X is fps (eg -fps60 for 60 fps)

