import sys

from daemon.app import Request_session as rS
from daemon.app.Parser import scrap_thread_data
from daemon.app.Scraper import WebScraper
from daemon.app.srv.ThreadSrv import ThreadSrv
from daemon.constants.fc_threads import HOME_URL, THREAD_URL


def run_project(args):
    print("Iniciando aplicación...")
    print("Límite marcado por el usuario:")
    # limit = args[1:]
    limit = int(input())

    ws = init_web_scraper()
    print("Iniciando servicios...")
    threadSrv = ThreadSrv()

    print("Verificando último thread guardado...")
    index = get_last_thread(threadSrv) + 1
    last_thread = index + limit

    print("Iniciando spider...")
    while (index <= last_thread):
        ws.parse_page(THREAD_URL.format(index))

        if not ws.is_invalid_thread():
            thread = scrap_thread_data(ws)
            threadSrv.create(thread)

        index = index + 1


def get_last_thread(thread_srv: ThreadSrv) -> int:
    last_thread = thread_srv.get_last_thread()
    if last_thread is None:
        return 0
    else:
        return last_thread.id


def init_web_scraper():
    print("Conecting to the website ", HOME_URL)
    cookie = rS.get_cookie()
    print("starting scraper...")
    return WebScraper(cookie)


if __name__ == '__main__':
    run_project(sys.argv)
