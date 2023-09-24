"""Retrieves static files.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.08
        revise for wsgi (16).
        add game controller (16).

.. versionadded::    20.07
        add version file.

.. versionadded::    20.07.1
        Support import from other files.

.. versionadded::    22.09
        Support import from other files.

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

"""
import bottle
from bottle import Bottle, redirect, request, get, static_file
# name and list your controllers here so their routes become accessible.
from . import img_dir, js_dir, css_dir, tpl_dir, gam_dir, py_dir
# Enable debugging, which gives us tracebacks
bottle.DEBUG = True

# Run the Bottle wsgi application. We don't need to call run() since our
# application is embedded within an App Engine WSGI application server.
appbottle = Bottle()


@appbottle.get('/x')
def home():
    """ Return Hello World at application root URL"""
    prj = request.query.proj
    print("home project /", prj)
    redirect('/main?proj=%s' % prj)


# Static Routes
@get("<_:re:.*favicon.ico>")
def favicon(_):
    return static_file("favicon.ico", root=img_dir)


# Static Routes
@get("/site/<filepath:re:.*\.(html|tpl)>")
def ajs(filepath):
    return static_file(filepath, root=tpl_dir)


# Static Routes
@get("/site/css/<filepath:re:.*\.(js|css)>")
def ajs(filepath):
    return static_file(filepath, root=css_dir)


# Static Routes
@get("/css/<filepath:re:.*\.(js|css|map)>")
def ajs(filepath):
    print("/css/<filepath:re:.*\.(js|css|map)>", css_dir)
    return static_file(filepath, root=css_dir)


@get("/view/<filepath:re:.*\.py>")
def ajs(filepath):
    print("/view/<filepath:re:.*\.(js|css|map)>", py_dir)
    return static_file(filepath, root=py_dir)


@get("/game/<filepath:re:.*\.html>")
def ajs(filepath):
    print("/css/<filepath:re:.*\.(js|css|map)>", css_dir)
    return static_file(filepath, root=gam_dir)


# Static Routes
@get("/js/<filepath:re:.*\.(js|css)>")
def ajs(filepath):
    return static_file(filepath, root=js_dir)


# Static Routes
@get("<filepath:re:.*\.(js|css)>")
def js(filepath):
    return static_file(filepath, root=js_dir)


# Static Routes
@get("/image/<filepath:re:.*\.(png|jpg|svg|gif|ico)>")
def img(filepath):
    return static_file(filepath, root=img_dir)


@appbottle.error(code=404)
def error_404(_):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'
