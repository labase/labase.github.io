#! /usr/bin/env python
# -*- coding: UTF8 -*-
# noinspection GrazieInspection
"""Criador de sites usando Teclemmino para HTML-CSS.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.11
        🌱 Criador de sites, Montagem inicial (06).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
VERSION = "version=23.11.06"
LOG_LEVEL = 0


class Log:
    def __init__(self, min_level=LOG_LEVEL):
        self.min_level = min_level

    def log(self, level, *args):
        print(*args) if level > self.min_level else None


LG = Log(LOG_LEVEL)


class Main:
    def __init__(self, br):
        self.tom_obj = None
        self.br = br
        self.site = ""
        self.a_map = {}
        self.macro = {}
        self.root = {}
        self.render() if br else None

    def nop(self, **kwargs):
        _ = self
        print("NOP: ", kwargs)
        return kwargs

    def lex(self, **kwargs):
        def function(tg):
            tg = tg.upper()[1:]
            return getattr(self.br, tg) if hasattr(self.br, tg) else lambda **kw: self.nop(tag_=tg, **kw)

        self.a_map = {alias: function(tag) for alias, tag in kwargs.items()}

    def parse_(self, tag_, **kwargs):
        _ = self.br

        _tag, *_id = tag_.split("_")
        if _tag in self.a_map and kwargs:
            return self.a_map[_tag](id=tag_, text={tg: self.parse_(tg, **kw) for tg, kw in kwargs.items() if
                                                   isinstance(kw, dict)})

            # self.a_map[_tag](id=tag_)
            # [self.parse_(tg, **kw) for tg, kw in kwargs.items() if isinstance(kw, dict)]
        else:
            print("END------>", _tag, _id)
            return

    def parse(self):
        # br = self.br
        to = self.tom_obj
        self.lex(**to["AMAP_0"])
        the_div = "DIV"
        tuples = [(alias, clazz) for root in to["ROOT"].values() for alias, clazz in root.items()]
        LG.log(1, tuples)
        self.a_map.update(
            {alias: lambda cl=clazz, **kw: self.nop(tag_=the_div, Class=cl, **kw) for alias, clazz in tuples})
        [map_(alias=alias_) for alias_, map_ in self.a_map.items()]
        print("<--------------***********", to["BD_ROOT"])
        [self.parse_(tag_=tg, **kw) for tg, kw in to["BD_ROOT"].items()]
        # [print(tg, **kw) for tg, kw in to["BD_ROOT"].items()]
        print("<--------------***********")

    def render(self):
        br = self.br
        br.template("_tt_").render(titulo="A V A N T A R 🐧")
        br.template("_version_").render(version=VERSION)
        # self.teclemmino = Teclemmino(br)

    def load(self, cfile=str('site.toml'), str_io=None):
        import tomlib
        # self.splash_screen()
        if str_io:
            self.site = str_io
            tom_obj = dict(tomlib.loads(self.site))
            tom_obj.pop("_")
            return True

        with open(cfile, "r") as avt:
            avt.seek(0)
            self.site = avt.read()
            self.tom_obj = tom_obj = dict(tomlib.loads(self.site))
        tom_obj.pop("_")
        # print("self.assets", self.assets)
        # self.start_game_from_root_element()
        # LG.log(4, "load_ ⇒ file_, cfile, str_io,: ⇒", cfile, str_io, "\n", self.site[200:400])
        LG.log(4, "load_ ⇒ file_, cfile, str_io,: ⇒", str_io, "\n", tom_obj)
        # self.splash_screen() if not str_io else self.start_game_from_root_element()
        self.parse()
        return str_io


def main(br):
    Main(br).load()


if __name__ == '__main__':
    main(None)
