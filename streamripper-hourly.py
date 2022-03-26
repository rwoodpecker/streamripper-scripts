import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    sw_output = []
    current_time = datetime.now()

    sw_output.append("ARTIST=" + str(current_time.year))
    sw_output.append("ALBUM=" + str(current_time.month))
    sw_output.append("TITLE=" + str(current_time.strftime("%Y-%m-%d_%H-%M-%S")))
    sw_output.append(".")
    sw_output = "\n".join(sw_output) + "\n"
    sys.stdout.write(sw_output)
    sys.stdout.flush()


ap_schedule = BlockingScheduler()
ap_schedule.add_job(job, trigger="cron", hour="*", minute="*/1")
ap_schedule.start()
