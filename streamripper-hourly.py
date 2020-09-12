#! /usr/bin/python

import sys
import time

# every 30 mins
DELAY = 1800

while True:
        out = []

        t = time.localtime()

        out.append("ARTIST=%d" % t.tm_year)
        out.append("ALBUM=%d" % t.tm_mon)
        out.append("TITLE=%d-%d-%d_%d-%d-%d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
        out.append('.')

        out = "\n".join(out) + "\n"

        sys.stdout.write(out)
        sys.stdout.flush()

        time.sleep(DELAY)
