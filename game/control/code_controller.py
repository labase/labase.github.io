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
"""Controller handles routes starting with /code.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    18.07
        Código inicial.

.. versionadded::    20.07.1
        Support import from other files.

"""
from bottle import static_file, HTTPError, Bottle, get  # , debug
from . import py_dir
from . import model_dir
from base64 import decodebytes as dcd
from model.datasource import DS
from github.GithubException import UnknownObjectException
__author__ = 'carlo'
DEFAULT_CODE = """# default
try:
    import superpython.%s.main as main
    main.main()
except:
    from browser import document, html
    document["pydiv"].html = ""
    document["pydiv"] <= html.IMG(src="/images/site_em_construcao_.jpg")
"""


# Static Routes
@get("<rota:path>/__init__.py")
def init_py(rota="nono"):
    print(f"initview_py-->/<{rota}>/__init__.py")
    return ""


# Static Routes
@get("/<:path>/__code/core/<filepath:re:.*[.]py>")
def core_py(filepath):
    print("core_py", filepath)
    return static_file(filepath, root=py_dir+"/core")


# Static Routes
@get("/__code/kwarwp/<filepath:path>")
def view_py(filepath):
    print("view_py", filepath)
    return static_file(filepath, root=py_dir+"/kwarwp")


# Static Routes
@get("/<:path>/__code/model/<filepath:path>")
def model_py(filepath):
    return static_file(filepath, root=model_dir)


# Static Routes
@get("/<:path>/__code/_spy/<module_name>/<filepath:re:.*[.]py>")
def spy(module_name, filepath):
    # print("_spy", module_name, filepath)
    try:
        code_file = DS.get_file_contents("_spy", module_name, filepath)
        code_str = dcd(str.encode(code_file.content)).decode("utf-8")
    except UnknownObjectException as _:
        # code_str = "# File not found"
        raise HTTPError(404)

    return code_str


@get("/<:path>/play/<project_name>/<parent_name>/__code/<mod:re:[a-z].*>/<filer:re:.*[.]py>")
def gamer_long(project_name, parent_name, mod, filer):
    modl, namel, filerl = mod.lower(), filer.lower(), filer.lower()
    project_name, parent_name, = project_name.lower(), parent_name.lower()
    # print(f"gamer_long - {parent_name} --->", project_name, modl, filerl)
    # noinspection PyBroadException
    try:
        code_file = DS.get_file_contents(project_name, modl, filerl)
        code_str = dcd(str.encode(code_file.content)).decode("utf-8")
        # code = dcd(str.encode(code_file.content)).decode("utf-8")
    except Exception:
        # print("Exception gamer_long", modl, namel, filerl)
        raise HTTPError(404)

        # code = HEADER.format(p=modl, m=namel, f=filerl, d=datetime.datetime.now().strftime("%y.%m"))
        # code = ecd(bytearray(code.encode("UTF8"))).decode("utf-8")
    return code_str


# Static Routes
@get("/<:path>/play/<project_name>/__code/<module_name:re:[a-z].*>/<filepath:re:.*[.]py>")
def local_spy(project_name, module_name, filepath):
    print("local_spyspy", project_name, module_name, filepath)
    try:
        code_file = DS.get_file_contents(project_name, module_name, filepath)
        code_str = dcd(str.encode(code_file.content)).decode("utf-8")
    except UnknownObjectException as _:
        # code_str = "# File not found"
        raise HTTPError(404)
    return code_str


# Static Routes
@get("/__code/core/__init__.py")
def init_py(rota=""):
    print(f"initview_py/{rota}/__init__.py")
    return ""


appbottle = Bottle()  # create another WSGI application for this controller and resource.
# debug(True)  # uncomment for verbose error logging. Do not use in production
