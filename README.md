# csvfilegraphingpython
Local graphing for csv files

This uses data gathered from a microbit - working on making it real time

Hey, 
This project doesn't require an internet connection however it doesn't
use default libraries if you want to use this you will need to install
matplotlib and pandas.
You can install these by heading to your terminal and running.
pip install pandas
and 
pip install matplotlib
you may have to use pip3 instead of pip but eh.
you can verify these installations by using the command
python -c "import pandas as pd; print(pd.__version__)"
yes it's long yes it's boring
you may need to specify python3 instead of python but shouldn't be an
issue unless using python 2 and 3 on the same machine.


Make sure you have pip installed btw. <3
and if it doesnt work and you're using python 3.11+ maybe an issue 
with an externally managed enviroment if so uhh do this

sudo rm/usr/lib/python3.11/EXTERNALLY-MANAGED

or

pip install package_name --break-system-packages

this was made the raspberry pi - personally im using the raspberry 
pi 2 32 bit

to run you'd probably need to navigate to the files home directory in
my case it's /home/user/Desktop/Project just grab it from the top of
the file explorer
to navigate you'd use cd /home/user/Desktop/Project 
then type python plot_data.py in your terminal

If you have any issues contact me on github Jack-Tlzo
