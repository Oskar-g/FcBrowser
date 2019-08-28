from daemon.app import Request_session as rS
from daemon.app.Parser import scrap_thread_data
from daemon.app.Scraper import WebScraper
from daemon.app.srv.ThreadSrv import ThreadSrv
from daemon.constants.fc_threads import HOME_URL, THREAD_URL, THREAD_BASE, START_INDEX, MAX_THREADS


def run_project():
    print("Iniciando aplicación...")

    print("Iniciando servicios...")
    thread_srv = ThreadSrv()
    ws = init_web_scraper()

    limit = get_limit(thread_srv)
    index = get_start_thread(thread_srv)
    last_thread = index + limit

    start_loop(index, last_thread, ws, thread_srv)


def start_loop(index, last_thread, ws, thread_srv):
    print("Iniciando spider...")
    while index <= last_thread:
        try:
            ws.parse_page(THREAD_URL.format(index))

            if not ws.is_invalid_thread() and ws.get_page_category() != THREAD_BASE:
                thread = scrap_thread_data(ws)
                if thread_srv.read(thread.id) is None:
                    thread_srv.create(thread)

        except:
            print("Ha sucedido un error inesperado, Entrada: ", index)

        index = index + 1


def get_limit(thread_srv):
    start = get_last_thread(thread_srv)
    maximum = MAX_THREADS - start
    print("Cuántos Hilos a escanear?: [{} default]".format(maximum))
    limit = input()
    if limit is None or limit == "" or not limit.isnumeric():
        limit = maximum

    return int(limit)


def get_start_thread(thread_srv):
    start = get_last_thread(thread_srv)
    print("Desde qué hilo empezamos?: [{} default]".format(start))
    key = input()
    if key is None or key == "" or not key.isnumeric():
        start = start + 1
    else:
        start = key
    return int(start)


def get_last_thread(thread_srv) -> int:
    last_thread = thread_srv.get_last_thread()
    if last_thread is None:
        return START_INDEX
    else:
        return last_thread[0]


def init_web_scraper():
    print("Conecting to the website ", HOME_URL)
    cookie = rS.get_cookie()
    print("starting scraper...")
    return WebScraper(cookie)


if __name__ == '__main__':
    run_project()
