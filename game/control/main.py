#! /usr/bin/env python
# -*- coding: UTF8 -*-
""" "Module defining mountings for bottle library.


"""
"""Module defining mountings for bottle library.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.08
        revise for wsgi (16).
        add game controller binder (16a).
        
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
from bottle import run, TEMPLATE_PATH, static_file, route, default_app
from . import play_controller
from . import inf_dir, tpl_dir
from . import static_controller
from . import code_controller
'''
from . import game_controller
from . import play_controller
from . import supygirls_controller
'''

# Create a new list with absolute paths
# TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))
# make sure the default templates directory is known to Bottle

if inf_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, tpl_dir)


@route('/')
def index():
    # print(inf_dir)
    # return "Today is a beautiful day"
    return static_file('index.html', root=inf_dir)


@route('/kwarwp')
def kwarwp():
    return static_file('kwarwp.html', root=tpl_dir)


application = default_app()
_ = application

# Mount a new instance of bottle for each controller and URL prefix.
# appbottle.mount("/external/brython/Lib/site-packages", project_controller.bottle)
# application.mount("/<:re:.*>/_spy", code_controller.bottle)
# application.mount("/<:path>/stlib", static_controller.appbottle)
# application.mount("/<:path>/image", static_controller.appbottle)
# application.mount("/<:path>/css", static_controller.appbottle)
# application.mount("/<:path>/site", static_controller.appbottle)
application.mount("/stlib", static_controller.appbottle)
application.mount("/<:re:.*>/image", static_controller.appbottle)
application.mount("/<:re:.*>/css", static_controller.appbottle)
application.mount("/<:re:.*>/game", static_controller.appbottle)
application.mount("/site", static_controller.appbottle)
# application.mount("/<:path>/play/<:re:.*>/__code/", code_controller.appbottle)
application.mount("/<:path>/play/", play_controller.appbottle)
# application.mount("/<:path>/__code/", code_controller.appbottle)
application.mount("/<:path>/play/<:path>/__code/", code_controller.appbottle)
# application.mount("/<:re:.*>/play/<:re:.*>/__code/", code_controller.appbottle)

# application.mount("/<:path>/__code/", code_controller.appbottle)
# application.mount("/<:re:.*>/edit", play_controller.appbottle)

# application.mount("/<:re:.*>/play/", play_controller.appbottle)
# application.mount("/<:re:.*>/supygirls/", supygirls_controller.appbottle)

if __name__ == "__main__":
    run(host='localhost', port=8080)
