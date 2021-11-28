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
<br>
If NOT in automate mode:
<br>
Use R to scramble list.
<br>
Use I to run insertion sorting algorithm.
<br>
Use B to run bubble sorting algorithm.
<br>

Program can take arguments when called from command line:
    <br>`--automate`: automate randomising and sorting in an infinite loop.
    <br>`--debug`: prints out some debug messages.
    <br>`-wX`: width of blocks, where X is width (eg -w10 for 10px wide blocks).
    <br>`-hX`: height of blocks, where X is height (eg -h0 for 1:1 ratio of pixels to int value).
    <br>`-fpsX`: fps to run at, where X is fps (eg -fps60 for 60 fps).
    <br>`-gX`: gap between blocks, where X is gap between blocks (eg -g0 for 0 pixel gap).

