#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SupyPlay
# Copyright 2010–2022 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.activufrj.nce.ufrj.br>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# SupyPlay é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>
"""Module defining mountings for bottle library.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    20.07
        add version file.

.. versionadded::    20.07.1
        Support import from other files.

.. versionadded::    22.09
        Support import from other files.

"""
from bottle import run, TEMPLATE_PATH, static_file, route, default_app
from . import play_controller
from . import tpl_dir
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

if tpl_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, tpl_dir)


@route('/')
def index():
    return static_file('index.html', root=tpl_dir)


@route('/kwarwp')
def kwarwp():
    return static_file('kwarwp.html', root=tpl_dir)


application = default_app()
_ = application

# Mount a new instance of bottle for each controller and URL prefix.
# appbottle.mount("/external/brython/Lib/site-packages", project_controller.bottle)
# application.mount("/<:re:.*>/_spy", code_controller.bottle)
application.mount("/<:path>/stlib", static_controller.appbottle)
application.mount("/<:path>/image", static_controller.appbottle)
application.mount("/<:path>/css", static_controller.appbottle)
application.mount("/<:path>/site", static_controller.appbottle)
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
