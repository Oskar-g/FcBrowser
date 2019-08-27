import ssl

from bs4 import BeautifulSoup
from requests.sessions import Session

from daemon.constants.beutifulSoup import SOUP_PARSER
from daemon.constants.fc_threads import DECORATOR, PRIVATE_PAGE_TITLE, INVALID_PAGE_TITLE


class WebScraper:

    def __init__(self, session: Session = None):
        self.session: Session = session
        self.soap = None
        self.__invalid_web = False
        self.__private_web = False
        self.url = ""

    def is_invalid_thread(self):
        return self.__invalid_web

    def is_private_web(self):
        return self.__private_web

    def parse_page(self, url: str = None) -> BeautifulSoup:
        """
        Obtener el dom de una url
        """

        if url is not None:
            self.url = url

        if "" == self.url:
            raise Exception("No se ha especificado URL:")

        page = self._get_page_content(self.url)

        if None is page:
            raise Exception("web no encontrada:", page)

        self.soap = BeautifulSoup(page.content, SOUP_PARSER)
        self._check_invalid_web()

        if not self.__invalid_web:
            self._check_private_web()

        return self.soap

    def _get_page_title(self) -> str:
        """
        Obtener el título de una página
        """

        title = self.soap.select_one('title').get_text()
        return self._clean_title(title)

    def _get_page_content(self, url):
        print("Abriendo direccion: " + url)

        if self.session is not None:
            print("Acceso por COOKIE")
            return self.session.get(url)

        print("Acceso por REQUEST")
        # Por algún motivo así no funciona...
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        # return urlopen(url, context=ctx)
        return None

    def _check_invalid_web(self) -> ():
        title = self._get_page_title()

        self.__invalid_web = False
        if INVALID_PAGE_TITLE == title:
            self.__invalid_web = True

    def _check_private_web(self) -> ():
        title = self._get_page_title()

        self.__private_web = False
        if PRIVATE_PAGE_TITLE == title:
            self.__private_web = True

    def get_page_index(self) -> int:
        if self.url == "":
            print("No se ha indicado URL")
            return 0

        index = self.url.split("=", 1)
        if len(index) != 2:
            print("No se pudo obtener el indice")
            return 0

        return int(index[1])

    def get_page_name(self) -> str:
        """
        Obtener el nombre de una página
        """
        if self.is_private_web() is True:
            return self._get_private_page_name()

        return self._get_open_page_name()

    def _get_open_page_name(self) -> str:
        """
        Obtener el nombre de una página abierta al público
        """

        name = self.soap.select_one('title').get_text()
        return self._clean_title(name)

    def _get_private_page_name(self) -> str:
        """
        Obtener el nombre de una página cerrada al público
        """
        name = self.soap.select_one('.mfont strong').get_text()
        return self._clean_title(name)

    def get_page_category(self) -> str:
        page_name = self.get_page_name()
        if page_name == "":
            print("No se pudo obtener la categoría")
            return ""

        category = self._iterate_decorators(page_name)

        if len(category) == 0:
            return "Normal"

        return ",".join(category)

    def get_page_url(self) -> str:
        return self.url

    def clean_status(self) -> ():
        self.session = None
        self.soap = None
        self.url = ""
        self.__private_web = False
        self.__invalid_web = False

    @staticmethod
    def _clean_title(title) -> str:
        title = title.split(" - ForoCoches")
        title = title[0].strip()
        return title

    @staticmethod
    def _iterate_decorators(page_name) -> []:
        category = []
        for key in DECORATOR:
            dec = str.upper(DECORATOR[key])
            if str.upper(page_name).find(key) >= 0:
                category.append(dec)

        return category
