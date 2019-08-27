from daemon.app import Scraper
from daemon.app.entities import Thread


def scrap_thread_data(scraper: Scraper):
    key = scraper.get_page_index()
    name = scraper.get_page_name()
    category = scraper.get_page_category()
    url = scraper.get_page_url()
    thread = Thread(key, name, category, url)
    return thread
