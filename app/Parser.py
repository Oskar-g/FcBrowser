from app.Scraper import WebScraper
from app.entities.Thread import Thread


def scrap_thread_data(scraper: WebScraper) -> Thread:
    key = scraper.get_page_index()
    name = scraper.get_page_name()
    category = scraper.get_page_category()
    url = scraper.get_page_url()
    return Thread(key, name, category, url)
