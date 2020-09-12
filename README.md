# streamripper-scripts

Use streamripper-hourly to create a new file for every hour of stream.

Call it with -E i.e.:

streamripper $url -o always -D "station_%D" -E "python /home/radio/streamripper-hourly.py"

More info at https://sourceforge.net/p/streamripper/discussion/19083/thread/c17fff31/.
