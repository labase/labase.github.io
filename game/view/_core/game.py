#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Game criado usando a interface declarativa Teclemmino.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.09
        Spike for Teclemmino (09).
        Spike for game test (08).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import unittest


class Teclemmino:
    def __init__(self, vito):
        self.vito = vito
        self.last ={}
        self.cmd = {k: v for k, v in zip("cet", [self.cena, self.elemento, self.texto])}
        self.assets = {}

    def cena(self, asset, **kwargs):
        self.assets[asset] = self.vito.Cena(nome=asset, **kwargs)
        # print("Vito -> cena", asset, kwargs)

    def elemento(self, asset, **kwargs):
        self.assets[asset] = self.vito.Elemento(nome=asset, **kwargs)
        # print("Vito -> elemento", asset, kwargs)

    def texto(self, asset, **kwargs):
        self.assets[asset] = self.vito.Texto(nome=asset, **kwargs)
        # print("Vito -> texto", asset, kwargs)

    def parse_(self, toml_obj):
        def go(cmd, name, **value):
            val = {k:v for k,v in value.items() if "-" not in k}
            self.last=name
            # print("go, cmd, name, value ->:", cmd, name, value)
            [self.parse_({sub:v}) for sub,v in value.items()if "-" in sub]
            self.cmd[cmd](name, **val)
            self.last = None
        toml_it = [key.split("-")+[value] for key, value in toml_obj.items()]
        print(toml_it)
        [go(cmd, name, **value) for cmd, name, value in toml_it]
        return True


class Main:
    def __init__(self, br):
        # from pathlib import PurePath
        import toml
        pp = str('view/_core/avantar.toml')
        with open(pp, "r") as avt:
            aavt = avt.read()
            x = toml.loads(aavt)
        y = [[l for l in k] for k in x]
        y= dict(x)

        # x = br.yaml.load("avantar.yaml")
        # print("br.yaml.load", y)
        br.template("_tt_").render(titulo="A V A N T A R 🐧")
        br.Cena("https://i.imgur.com/9M9k6RZ.jpg").vai()
        br.Elemento(img="")
        Teclemmino(br).parse_(y)


def main(br):
    Main(br)


if __name__ == '__main__':
    unittest.main()
