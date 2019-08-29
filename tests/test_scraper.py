import unittest

from requests.sessions import Session

from app import Request_session as rS
from app.Scraper import WebScraper


class SessionTest(unittest.TestCase):

    def test_page_is_invalid(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=1")
        self.assertTrue(ws.is_invalid_thread())

    def test_page_is_private(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7383804")
        self.assertTrue(ws.is_private_web())

    def test_page_is_public(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7309366")
        self.assertFalse(ws.is_private_web())

    def test_page_conection(self):
        ws = WebScraper(Session())
        # url +HD
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7373097")
        self.assertTrue(ws.is_private_web())

        # añadir cookie de sesion a scraper para tener acceso a +HD
        cookie = rS.get_cookie()
        ws.session = cookie
        ws.parse_page()
        self.assertFalse(ws.is_private_web())

    def test_get_categories(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7373097")
        self.assertEqual(ws.get_page_category(), "+HD,+ENCUESTA")

    def test_get_page_name_is_valid(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7383485")
        text = ws.get_page_name()
        self.assertEqual(text, "Nativa del AMAZONAS viendo como QUEMAN SU PUEBLO y llorando de rabia")

    def test_get_page_index_is_null(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        text = ws.get_page_index()
        self.assertEqual(text, 0)

    def test_get_page_index_is_valid(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7383485")
        text = ws.get_page_index()
        self.assertEqual(text, 7383485)

    def test_clean_Scraper(self):
        cookie = rS.get_cookie()
        ws = WebScraper(cookie)
        ws.parse_page("https://www.forocoches.com/foro/showthread.php?t=7383485")
        ws.clean_status()
        self.assertEqual(ws.url, "")
        self.assertEqual(ws.session, None)
        self.assertEqual(ws.soap, None)
        self.assertFalse(ws.is_private_web())
