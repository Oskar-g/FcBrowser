#!/usr/bin/python
import requests

from daemon.constants import fc_threads


def get_cookie() -> requests.sessions.Session:
    with requests.Session() as s:
        s.post(fc_threads.LOGIN_SUBMIT,
               data={
                   "do": "login",
                   "forceredirect": 1,
                   "url": "/",
                   "vb_login_md5password": "",
                   "vb_login_md5password_utf": "",
                   "s": "",
                   "securitytoken": "guest",
                   "vb_login_username": fc_threads.USER,
                   "vb_login_password": fc_threads.PASSWORD,
                   "cookieuser": 1,
                   "logb2": "Acceder"
               })

    print("Generando cookie de acceso...")

    return s