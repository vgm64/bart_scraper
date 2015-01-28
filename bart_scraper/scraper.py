""" Scraping.
"""

from bart_api import BartApi
import datetime


class BartScraper(BartApi):
    def __init__(self, api_key="MW9S-E7SL-26DU-VV8V"):
        super(BartScraper, self).__init__(api_key)
        self.all_stations = None
        self.stn_by_abbr = None

    def initialize_bart_info(self):
        self.all_stations = self.get_stations()
        self.stn_by_abbr = {}
        for stn in self.all_stations:
            self.stn_by_abbr['abbr'] = stn

    # def get_next_scrape_time(self):
    #     return datetime.datetime.now() + datetime.timedelta(seconds=60)

    def scrape_departure_times(self):
        etd = self.etd(station='ALL')
        # self.write(etd)
        return etd

    def write_to_stdout(self, *args):
        print args

    def write(self, *args):
        self.write_to_stdout(args)


