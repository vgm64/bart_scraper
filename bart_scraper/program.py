"""

"""
import datetime

from scraper import BartScraper
from db import BartDB
from scheduler import on_the
from logging import log


class BartProgram(object):
    def __init__(self):
        self.scraper = None
        self.db = None

    def go(self):
        timestamp = datetime.datetime.now()
        trains = self.scraper.scrape_departure_times()
        self.db.insert(timestamp, trains)

    def run(self):
        self.scraper = BartScraper()
        self.db = BartDB(engine='sqlite3', db='./bart.db')
        self.scraper.initialize_bart_info()

        time_range = datetime.time(22, 22, 30), datetime.time(23, 28, 25)

        while True:
            log("GLOBAL START")
            on_the('second', self.go, time_range)




if __name__ == '__main__':
    try:
        BartProgram().run()
    except KeyboardInterrupt:
        log("Exiting.")
