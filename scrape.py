import requests
import scrapy
from bs4 import BeautifulSoup


class Scraper:
    source = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show="

    def scrape(self, name, season_from, season_to, saving_dir):
        print("Starting the scrape...")
        from_ = int(season_from)
        to_ = int(season_to)
        # seasons
        episode_number = 1
        has_episode = True
        for i in range(from_, to_):
            while has_episode:
                print("Scraping season", i, "episode", episode_number, "...")
                link_address = self.source + name + "&episode=s" + self.number_to_str(i) + "e" + self.number_to_str(
                    episode_number)
                soup = BeautifulSoup(self.connect_to_page(link_address), 'html.parser')
                if self.is_valid_episode(soup):
                    script = self.get_script(soup)
                    print("####### SEASON", i, "EPISODE", episode_number, "SCRIPT: #########3")
                    print(script)
                else:
                    break
                episode_number += 1

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

    @staticmethod
    def is_valid_episode(soup):
        search_page = soup.find_all('div', {'class': 'search-and-alpha'})
        if len(search_page) is 0:
            return True
        else:
            return False

    @staticmethod
    def get_script(soup):
        return soup.find_all('div', {'class': 'scrolling-script-container'})
