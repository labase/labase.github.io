#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Game criado usando a interface declarativa Teclemmino.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.09
        Fix Texto popup with new class (10).
        Spike for Teclemmino (09).
        Spike for game test (08).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import logging
import unittest
from collections import namedtuple as ntp

SEP = "_"
One = ntp("One", "d f a i s h h1")
Two = ntp("Two", "p b hd sc fm fs ip lg lb ft")
LD = logging.debug
W, H = 1350, 650
IMGSIZE, IMG_HEIGHT = f"{32 * W}px", f"{4 * H}px"


class Teclemmino:
    def __init__(self, vito):
        STYLE, NADA, NDCT, NoEv = vito.STYLE, vito.NADA, vito.NDCT, vito.NoEv
        STYLE['width'] = 1350
        html = vito.html
        self.tag_one = One(html.DIV, html.FIGURE, html.A, html.IMG, html.SPAN, html.H4, html.H1)
        self.tag_two = Two(html.P, html.BUTTON, html.HEADER, html.SECTION, html.FORM,
                     html.FIELDSET, html.INPUT, html.LEGEND, html.LABEL, html.FOOTER)
        teclemmino = self

        class Folha:
            # def __init__(self, img, nome=None, **kwargs):
            def __init__(self, img, dimensions:list, nome=None, **kwargs):
                _ = nome, kwargs
                print("Folha", dimensions)
                # dimensions = [4,4]
                self.dim = d = ntp("Dimensions", "dx dy")(*dimensions)
                self.img = img
                self.style = {"max-width": f"{d.dx*100}%", "max-height": f"{d.dy*100}%"}
            def get_image(self, index):
                position = f"-{index % self.dim.dx * 100}% -{index // self.dim.dx * 100}%"
                self.style["background-position"] = position
                return dict(img=self.img, style=self.style)

        class Sprite(vito.Elemento):
            def __init__(self, img="", vai=None, style=NDCT, tit="", alt="",
                         x=0, y=0, w=100, h=100, o=1, texto='', foi=None, index=0, sw=100, sh=100, cx=1, b=0, s=1,
                         cena="", score=NDCT, drag=False, drop=NDCT, tipo="100% 100%", **kwargs):
                _ = style, score, tipo, drag, drop
                # style=dict(left=x, top=x, width=f"{w}px", height=f"{h}px", overflow="hidden", filter= f"blur({b}px)", scale=s)
                style = dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter=f"blur({b}px)", scale=s)
                position = f"-{index % cx * w}px -{index // cx * w}px"
                style.update({"max-width": f"{sw}px", "max-height": f"{sh}px", "background-position": position})

                super().__init__(img=img, vai=vai, tit=tit, alt=alt,
                                 x=x, y=y, w=w, h=h, o=o, texto=texto, foi=foi,
                                 style=style, cena=cena, tipo=f"{sw}px {sh}px",
                                 **kwargs)

                self._texto = Texto(texto, foi=self._foi) if texto else None
                self.vai = self._texto.vai if texto else self.vai

            def _do_foi(self):
                _texto = self.texto if self.tit else self.title  #else CORRECT.format(self.tit)
                self.vai = Texto( _texto, self.cena).vai
                LD(_texto, self.vai)

        class CenaSprite(vito.Cena):
            def __init__(self, img, index=0, **kwargs):
                super().__init__(img, **kwargs)
                # style=dict(left=x, top=x, width="80px", height="80px", overflow="hidden")
                style = dict(position="relative", left=f"-{index % 8 * W}px", top=f"-{(index % 16) // 4 * H}px",
                             width=f"{W}px",
                             height=f"{H}px", overflow="hidden", minWidth=IMGSIZE, minHeight=IMG_HEIGHT)
                div_sty = dict(STYLE)
                div_sty.update({"max-width": f"{W}px", "max-height": f"{H}px", "overflow": "hidden"})
                self.elt = html.DIV(style=div_sty)
                self.img = html.IMG(src=img, width=W, height=H, style=style)
                _ = self.elt <= self.img
                self._cria_divs(W)

        class SpriteSala(vito.Salao):
            def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, nome='', **kwargs):
                self.cenas = [n, l, s, o]
                self.nome = nome
                _ = kwargs
                self.p()

        class Texto:
            DOIT = True
            def __init__(self, tit="", txt="", cena=NADA, foi=None, nome=None, **kwargs):

                def dom(exi=None, mod=None):
                    d, f, a, i, s, h, h1 = list(teclemmino.tag_one)
                    p, b, hd, sc, fm, fs, ip, lg, lb, ft = list(teclemmino.tag_two)
                    card = d(
                        d(hd(p(tit, Class="modal-card-title") +
                             (closer := b(Class="delete", id=exi, ariaLabel="close")), Class="modal-card-head") +
                          sc(d(fm(
                              fs(lg(txt)),
                              Class="form-horizontal"), Class="content"), Class="modal-card-body"),
                          Class="modal-card"),
                        Class="modal", id=mod)
                    closer.bind("click", self.close_modal)
                    return card

                self.cena = cena
                self.kwargs = kwargs
                self.esconde = foi if foi else self.esconde
                self.tit, self.txt, self.nome = tit, txt, nome
                self.modal = dom("modal_closer_", "modal_popup_")
                self.deploy()

            def deploy(self, document=None):
                print("deploy", document)
                document = document or teclemmino.vito.document
                _ = document <= self.modal
                # noinspection PyAttributeOutsideInit
                self.deploy = lambda *_: None
            def close_modal(self, ev):
                ev.stopPropagation()
                ev.preventDefault()
                self.esconde()
                self.modal.classList.remove('is-active')

            def esconde(self):
                ...

            def mostra(self):  # , tit="", txt="", act=None, **kwargs):
                self.deploy()
                self.modal.classList.add('is-active')

            def vai(self, ev=NoEv()):
                ev.stopPropagation()
                ev.stopPropagation()
                self.mostra()  # self.tit, self.txt, act=self.esconde)
                return False

        self.vito = vito
        self.assets = {}
        self.last ={}
        classes = (CenaSprite, Sprite, SpriteSala, Texto, Folha)
        self.cmd = self.vito_element_builder(vito, classes)

    def vito_element_builder(self, v, classes):
        v.CenaSprite, v.Sprite, v.SpriteSala, v.Textor, self.vito.Folha = classes
        builder = [self.cena, self.elemento, self.texto, self.cena_sprite, self.sprite,
                   self.sprite_sala, self.folha, self.valor, self.icon]
        return {k: v for k, v in zip(['c', 'e', 't', 'r', 's', 'l', 'f', 'v', "i"], builder)}

    def cena(self, asset, **kwargs):
        self.assets[asset] = self.vito.Cena(nome=asset, **kwargs)
        self.last= asset
        # logging.debug("Vito -> cena", asset, kwargs)

    def sprite_sala(self, asset, **kwargs):
        self.assets[asset] = self.vito.SpriteSala(nome=asset, **kwargs)
        # logging.debug("Vito -> cena", asset, kwargs)

    def cena_sprite(self, asset, **kwargs):
        self.assets[asset] = self.vito.CenaSprite(nome=asset, **kwargs)
        self.last= asset
        # logging.debug("Vito -> cena_sprite", asset, kwargs, self.last)

    def sprite(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        # logging.debug("elemento kwargs", kwargs, self.last)
        self.assets[asset] = self.vito.Sprite(nome=asset, **kwargs)
        # logging.debug("Vito -> cena", asset, kwargs)

    def elemento(self, asset, **kwargs):
        # kwargs.update(**asset) if isinstance(asset, dict) else None
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        # print("elemento kwargs:->", asset, kwargs)
        # logging.debug("elemento kwargs", kwargs)
        # self.assets[asset] = self.vito.Elemento(nome=asset, **kwargs)
        self.assets[asset] = self.vito.Sprite(nome=asset, **kwargs)
        # logging.debug("Vito -> elemento", asset, kwargs)

    def texto(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        self.assets[asset] = t = self.vito.Textor(nome=asset, one=self.tag_one, two=self.tag_two, **kwargs)
        t.deploy(self.vito.document.body)
        # logging.debug("Vito -> texto", asset, kwargs)

    def valor(self, asset, **value):
        self.assets[asset] = dict(**value)
        print("Vito asset, value, self.assets[asset] -> valor: ", asset, value, self.assets[asset])
    def folha(self, asset, **kwargs):
        img = self.assets[asset]
        for at, fl in kwargs.items():
            img[at]=(self.vito.Folha(img[at], fl, nome=at))
        # _ = [img[at].put(self.vito.Folha(img[at], fl, nome=at)) for at, fl in kwargs.items()]
        print("def folha(self, asset, **kwargs->", asset, img)
        # self.assets[asset] = t = self.vito.Folha(asset, nome=asset, **kwargs)
    def icon(self, asset, item, index=None):
        print("icon:->", asset, item, index, self.assets)
        element = self.assets[asset][item]
        value = element.get_image(index=index) if hasattr("get_image", element) else element
        return value

    def parse_(self, toml_obj):
        DOT = "."
        def parse_key(key:str, dot=DOT):
            print("parse_key key: ->", key)
            def get_parts(key_, sep=SEP):
                tag, *parts = key_.split(sep)
                # print("parse_key get_parts: ->", key, tag, SEP.join(parts))
                return tag[0], sep.join(parts)
            if key.startswith(dot):
                key = key[1:]
                cmd, name, tag, *index = key.split(dot)
                index = dict(index=index[0]) if index else {}
                result = self.cmd[cmd](name, item=tag, **index)
                print("parse_key get_parts: ->", cmd, name, index, f">{result}<")

                return result
            else:
                return list(get_parts(key)) if SEP in key else key
        def go(cmd, name, **value_):
            #@@ FIX
            val = {k:parse_key(v) if isinstance(v, str) else v for k,v in value_.items() if SEP not in k}
            # val = {k:v for k,v in value_.items() if SEP not in k}
            print("cmd, name, value,: ->", cmd, name, value_, val)
            self.cmd[cmd](name, **val)
            [self.parse_({sub:v}) for sub,v in value_.items() if SEP in sub]            # self.last=name
            self.last = None
        # toml_it = [key.split(SEP) + [value] for key, value in toml_obj.items() if SEP in key]
        toml_it = [parse_key(key) + [value] for key, value in toml_obj.items() if SEP in key]
        [go(cmd, name, **value) for cmd, name, value in toml_it]
        return True
    def load_(self, cfile=str('view/_core/avantar.toml')):
        import toml
        with open(cfile, "r") as avt:
            tom_obj = dict(toml.loads(avt.read()))
            self.parse_(tom_obj)
            # print("self.assets", self.assets)
        self.start_game_from_root_element()
        return True

    def start_game_from_root_element(self):
        self.assets["ROOT"].vai() if "ROOT" in self.assets else None


class Main:
    def __init__(self, br):
        # from pathlib import PurePath
        # y = [[l for l in k] for k in x]
        # y= dict(x)
        br.template("_tt_").render(titulo="A V A N T A R 🐧")
        # br.Cena("https://i.imgur.com/9M9k6RZ.jpg").vai()
        # br.Elemento(img="")
        self.teclemmino = Teclemmino(br)
        self.br = br
    def load(self, cfile=str('view/_core/avantar.toml')):
        _ = cfile
        self.teclemmino.load_()


def main(br):
    Main(br).load()


if __name__ == '__main__':
    unittest.main()
