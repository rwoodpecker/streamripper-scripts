# streamripper-scripts

## Update 2022-03-27

Updated for python3 and uses apscheduler for extreme precision of splitting files. Splits files at the 00:00 of every hour. No more clock drift from long sleeps.

pip3 install apscheduler and run using python3.


streamripper-hourly-py2.py should only be used on systems where python3 is not available. It will suffer from clock drift on long sleeps causing innacurate splitting of files.

---

Use streamripper-hourly to create a new file for every hour of stream.

Call it with -E i.e.:

streamripper $url -o always -D "station_%D" -E "python /home/radio/streamripper-hourly.py"

More info at https://sourceforge.net/p/streamripper/discussion/19083/thread/c17fff31/.
