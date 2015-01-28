from bart_api import BartApi
from logging import log
import time
from datetime import datetime, timedelta
from threading import Timer

one_day = timedelta(hours=24)


def next_time(clock_point, offset=1):
    """ Return the (datetime, seconds) tuple for the next time to run. """
    now = datetime.now()
    then = now
    if clock_point == 'hour':
        then = then.replace(minute=0)
        then = then.replace(second=0)
        then = then.replace(microsecond=0)
        then = then + timedelta(seconds=3600+offset)
    elif clock_point == 'minute':
        then = then.replace(second=0)
        then = then.replace(microsecond=0)
        then = then + timedelta(seconds=60+offset)
    elif clock_point == 'second':
        then = then.replace(microsecond=0)
        then = then + timedelta(seconds=offset)

    sleep_time = (then - now).total_seconds()
    return then, sleep_time


def wait_until_in_range(time_range):
    start, end = time_range
    now = datetime.now()
    today, now_time = now.date(), now.time()


    log("Consider this...")
    log(start, "<", now_time, "<", end)
    # We are within range.
    if start < now.time() < end:
        log("In range.")
        time_to_sleep = timedelta()
    if now.time() < start:
        log("Before start")
        time_to_sleep = datetime.combine(today, start) - now
    if now.time() > end:
        log("After end")
        time_to_sleep = datetime.combine(today, start) + one_day - now

    log("Need to sleep", time_to_sleep.total_seconds(), "seconds.")
    time.sleep(time_to_sleep.total_seconds())


def on_the(sched, func, time_range=None):
    if time_range:
        wait_until_in_range(time_range)
    execution_time, sleep_time = next_time(sched)
    log("I know to sleep for", sleep_time, "before executing.")
    time.sleep(sleep_time)
    log("Executing func.")
    func()


if __name__ == '__main__':
    while True:
        dt, t = next_time('second')
        now = datetime.now()
        print "I'm good", now, now.microsecond, dt, t
        time.sleep(t)
