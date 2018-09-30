import requests
import scrapy
from bs4 import BeautifulSoup


class Scraper:
    source = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show="

    def scrape(self, name, season_from, season_to, saving_dir):
        from_ = int(season_from)
        to_ = int(season_to)
        # seasons
        episode_number = 0
        for i in range(from_, to_):
            link_address = self.source + name + "&episode=s" + self.number_to_str(i) + "e"
            soup = BeautifulSoup(self.connect_to_page(), 'html.parser')
        pass

    @staticmethod
    def connect_to_page(url):
        page = requests.get(url)
        page_text = page.text
        return page_text

    @staticmethod
    def number_to_str(number):
        if number < 10:
            return "0" + str(number)
        else:
            return str(number)

    def check_valid_episode(self):
        pass
