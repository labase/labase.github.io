#! /usr/bin/env python
# -*- coding: UTF8 -*-
# noinspection GrazieInspection
"""Game criado usando a interface declarativa Teclemmino.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.10
        🔨 fix extra, sorteio do cubo (19).
        ⛲ 🗃️ redireciona TOML (18 a).
        🧑‍🔬 Nome de Estação, Inicia TOML (18).
        ⛲ 🗃️ Inclui arquivos TOML (17).
        🧩 🗑️ Incluir trash game (16).
        🎏 Pique WebRTC (15 a).
        ☣️ Dificuldade dos jogos (15).
        ⛲ Inventário pega (13 a).
        🔨 🧩 Fix side games Cubo (13).
        🧩 Incluir side games Cubo (11 a).
        ⛲ Card automático de missão, posição e imagem (11).
        ⛲ Editor online de TOML (10).
        🏭 Reformata puzzle com cena automática (05).
        🔨 fix lançamento do texto, not yet (04).
        ⛲ Desiste de Missões (03).
        🏅 Inclui medalhas no inventário (02).
        ⁉️ Incluir Questões de texto (01).

.. versionadded::    23.09
        🧩 Incluir side games Puzzle de troca (24).
        🎱 Pool central de missões (23).
        Sprite Labirinto working (18).
        Sprite foi working, SpriteSala & Elemento.cena (16).
        Cena as Background (14).
        Declaration and retrieve for sprite element (13).
        Fix Texto popup with new class (10).
        Spike for Teclemmino (09).
        Spike for game test (08).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import unittest
from collections import namedtuple as ntp
from typing import List

VERSION = "version=23.10.19"
FLARE_ = "https://imgur.com/gQgpUFg.gif"
FLARE = "9CSpt5C"
# noinspection SpellCheckingInspection
CUBE_SIDES = ["t4bBEOI" "5WoBpmz" "XGjZLS8" "VrYCtas" "tt37M2J" "ZbCzZFb"]
WIDTH = 1350
Dim = ntp("Dimensions", "dx dy")
D11 = ntp("Dimensions", "dx dy")(1, 1)
SEP = "_"
One = ntp("One", "d f a i s h h1")
Two = ntp("Two", "p b hd sc fm fs ip lg lb ft")
W, H = 1350, 650
LOG_LEVEL = 7
IMGSIZE, IMG_HEIGHT = f"{32 * W}px", f"{4 * H}px"
# noinspection SpellCheckingInspection
A2J = "abcdefghij".upper()
LIXO = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/lixocenter.svg"
RUBBISH = "https://i.imgur.com/fCEvaqu.png"
R_OFF_X, R_OFF_Y, TOFF, SCAL = 625, 380, 10, 2.5
Hero = ntp("Hero", "luck pers level")
# noinspection SpellCheckingInspection
lixo = ['mala', 'chaves', 'escova', 'isqueiro', 'suco', 'vinil', 'baralho', 'dez',
        'eifell', 'porquinho', 'bule', 'luva', 'panda', 'cafe', 'guitarra', 'aranha',
        'livro', 'soldado', 'garrafa', 'pizza', 'fone', 'microfone', 'plug', 'visa', 'lata', 'moeda', 'carro', 'sino',
        'presente', 'ipod', 'clarineta', 'cinquenta', 'sujeira', 'blob', 'sujo',
        'facao', 'copinho', 'espremedor', 'pandeiro', 'sacola', 'latao', 'pimenta', 'areia',
        'regar', 'latinha', 'casca', 'hd', 'tenis', 'filme', 'ampulheta', 'pimentao',
        'bumerangue', 'relogio_pulso', 'relogio', 'oculos', 'martelo', 'faca', 'joaninha',
        'radio', 'bussola', 'chapeu', 'alicate', 'trolha', 'tamborim', 'pelucia', 'formiga',
        'jornal', 'chave_fenda', 'vidro', 'cd', 'calculadora', 'lapiseira', 'lampada', 'diploma',
        'lapis', 'tesoura', 'disquete', 'escorpiao', 'bife', 'lagosta', 'pera', 'cubo', 'canivete',
        'pulover', 'banana', 'tampinha', 'cantil', 'rolha', 'fava', 'vaso', 'vinho', 'bola',
        'dalia', 'saco', 'melancia', 'azeitona', 'limao', 'hotdog', 'cachecol', 'papel', 'pote',
        'picareta']


class Log:
    def __init__(self, min_level=LOG_LEVEL):
        self.min_level = min_level

    def log(self, level, *args):
        print(*args) if level > self.min_level else None


LG = Log(LOG_LEVEL)


class Teclemmino:
    def __init__(self, vito):
        # noinspection SpellCheckingInspection
        STYLE, NADA, NDCT, NoEv = vito.STYLE, vito.NADA, vito.NDCT, vito.NoEv
        STYLE['width'] = WIDTH
        html = vito.html
        self.I = html.I
        self.tag_one = One(html.DIV, html.FIGURE, html.A, html.IMG, html.SPAN, html.H4, html.H1)
        self.tag_two = Two(html.P, html.BUTTON, html.HEADER, html.SECTION, html.FORM,
                           html.FIELDSET, html.INPUT, html.LEGEND, html.LABEL, html.FOOTER)
        teclemmino = self

        class WebRTC:
            def __init__(self):
                self.channel = self
                self.connect()

            def publish(self, *_):
                pass

            def connect(self):
                def msg(_message):
                    vito.INV.cena.marquee(_message.data)

                try:
                    from env import ABLY

                    ably_pr = vito.ably
                    ably = ably_pr.Realtime.Promise.new(ABLY)
                    ably.connection.once('connected')
                    print('Connected to Ably!')
                    self.channel = channel = ably.channels.get('quickstart')
                    channel.subscribe('greeting', msg)
                except ImportError:
                    pass

            def envia(self, message="hello!", *_):
                self.channel.publish('greeting', message)

        self.rtc = WebRTC()

        class Folha:
            # def __init__(self, img, nome=None, **kwargs):
            def __init__(self, img, dimensions: list, nome=None, **kwargs):
                _ = nome, kwargs
                LG.log(2, "Folha", dimensions)
                # dimensions = [4,4]
                self.dim = d = ntp("Dimensions", "dx dy")(*dimensions)
                self.img = img
                # self.style = {"max-width": f"{d.dx * 100}%", "max-height": f"{d.dy * 100}%"}
                self.style = {"backgroundSize": f"{d.dx * 100}% {d.dy * 100}%"}

            def get_image(self, index):
                index = int(index)
                # position = f"{index % self.dim.dx * (100/ self.dim.dx)}% {index // self.dim.dx * (100/self.dim.dy)}%"
                position = f"{index % self.dim.dx * 100}% {index // self.dim.dx * 100}%"
                # self.style["background-position"] = position
                self.style.update(**{"backgroundPosition": position})
                return dict(img_=self.img, style_=self.style, dim_=self.dim)

        class Sprite(vito.Elemento):
            def __init__(self, img="", vai=NADA.vai, style=NDCT, tit="", alt="", put=False,
                         x=0, y=0, w=100, h=100, o=1, texto='', foi=None, b=0, s=1,
                         cena=NADA, score=NDCT, drag=False, drop=NDCT, tipo="100% 100%", **kwargs):
                _style = style
                from copy import deepcopy
                self.img_ = deepcopy(img) if isinstance(img, dict) else img
                style_ = {}
                # txt = _kwa["texto"] if "texto" in _kwa else {}

                LG.log(4, "Vito ⇒ Sprite texto⇒", texto if isinstance(texto, str) else "_nada_", tit) if put else None

                def _go():
                    self.w = self.h = 30
                    self.elt.style.backgroundSize = "30px 30px;"
                    self.siz = (30, 30)
                    teclemmino.vito.INV.bota(self)
                    self.elt.style = dict(backgroundSize="30px 30px;")
                    return foi

                def to_int(key):
                    LG.log(4, _style)
                    return [int(cdd[:-1]) for cdd in _style[key].split()]

                go = foi if not put else _go

                # gone = foi() if callable(foi) else go
                _ = score, drag, drop, tipo
                img_, _style, _dim = [v for v in img.values()] if isinstance(img, dict) else (img, {}, D11)
                if _style:
                    (ox, oy), (dx, dy) = to_int("backgroundPosition"), to_int("backgroundSize")
                    style_["backgroundPosition"] = f"{-ox / 100 * w}px {-oy / 100 * h}px"
                    style_["backgroundSize"] = "100% 100%" if put else f"{dx / 100 * w}px {dy / 100 * h}px"

                style = dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter=f"blur({b}px)", scale=s)
                LG.log(4, style)
                style.update(**style_)
                style.update(**{"background-image": f"url({img_})"})
                # noinspection PyCallingNonCallable
                cena = cena() if callable(cena) else cena
                LG.log(3, "Sprite(vito.Elemento) ⇒", img, foi, cena, style)

                super().__init__(img=img, vai=vai, tit=tit, alt=alt,
                                 x=x, y=y, w=w, h=h, o=o, texto=texto, foi=go,
                                 style=style, cena=cena, tipo="100% 100%",
                                 **kwargs)

                if img_.startswith("*"):
                    icon = teclemmino.I(Class=img[1:], style={"position": "relative", "color": "grey"})
                    _ = self.elt <= icon
                # self._texto = Texto(texto, foi=self._foi) if texto else None
                if isinstance(texto, dict):
                    self._texto = Texto(foi=go, **texto)
                else:
                    self._texto = Texto(texto, foi=go) if texto else None
                self.vai = self._texto.vai if texto else self.vai
                self.o = self.o_ = o

            def as_card(self):
                return self

            def copy(self):
                s = self
                attr = "img vai tit alt texto foi x y w h o".split()
                mtd = [s.img_, s.vai, s.tit, s.alt, s.texto, s.foi, s.x, s.y, s.w, s.h, s.o_]
                return {atn: atv for atn, atv in zip(attr, mtd)}

            def _do_foi(self):
                _texto = self.texto if self.tit else self.title  # else CORRECT.format(self.tit)
                self.vai = Texto(_texto, self.cena).vai
                LG.log(3, _texto, self.vai)

        class CenaSprite(vito.Cena):
            # noinspection SpellCheckingInspection
            def __init__(self, img, index=-1, direita="", local="", **kwargs):
                _style_ = {"backgroundSize": f"{8 * 100}% {8 * 100}%"}
                self.foi_evs = []
                self.local = local

                def parse_img(img_=img, style_=None, dim_=D11):
                    return img_, style_ or _style_, dim_

                _img_, _style_, _dim = parse_img(**img) if isinstance(img, dict) else (img, _style_, D11)
                style = dict(width=f"{W}px", height=f"{H}px", overflow="hidden")
                position = f"{index % _dim.dx * 100}% {index // _dim.dx * 100}%"
                _style_.update(backgroundPosition=position) if index > 0 else None
                style.update(**_style_)
                style.update(**{"background-image": f"url({_img_})"})

                super().__init__("", **kwargs)
                self.nome = kwargs["nome"] if "nome" in kwargs else _img_

                self.elt.html = ""
                self.elt.style = style
                self.cards = []
                if direita:
                    ptl = self.portal(L=teclemmino.parser(direita)())
                    LG.log(4, "CenaSprite direita", direita, self.nome, ptl)
                localidade = f" : {self.local}" if self.local else ""
                self.loc = loc = ".".join(self.nome.split("zz")[-2:])+localidade if "zz" in self.nome else "@@"
                # self.elt <= vito.html.MARQUEE(f"Local : {loc}")
                self.mrq = mrq = vito.document.createElement("marquee")
                mrq.text = f"Local : {loc}"
                mrq.setAttribute("scrollamount", "5")
                # mrq.setAttribute("bgcolor", "rgba(0.4,200,200,200)")
                # mrq.setAttribute("bgcolor", "rgba(200,200,200,0.4)")
                # mrq.setAttribute("bgcolor", "#AAA4")
                mrq.style.backgroundColor = "#AAAAAA55"
                mrq.style.marginTop = "35px"
                mrq.style.marginLeft = "200px"
                mrq.style.marginRight = "200px"
                # mrq.loop = 5
                _ = self.elt <= mrq

            # noinspection SpellCheckingInspection
            def marquee(self, text, scroll_amount=5):
                def on_finish(*_):
                    self.mrq.text = "Local:" + self.loc
                    # noinspection SpellCheckingInspection
                    self.mrq.setAttribute("scrollamount", scroll_amount)
                    self.mrq.loop = -1
                    self.mrq.start()

                self.mrq.bind("finish", on_finish)
                # self.mrq.bind("onfinish", on_finish)
                self.mrq.setAttribute("scrollamount", "20")
                # print("marquee", text)
                if 'emergência' in text:
                    print(text)
                    fl = vito.Elemento(f"https://i.imgur.com/{FLARE}.gif", x=1000, y=0, o=0.2, w=350, h=650, cena=self)
                    fl.o = 0.6
                    fl.elt.style.pointerEvents = "none"

                    # fl = teclemmino.vito_weather_overlay(vito,self,0.8,FLARE)
                self.mrq.text = text + self.loc
                self.mrq.loop = 1

            def __le__(self, other):
                self.cards.append(other.as_card()) if (hasattr(other, "as_card")) else None
                n_cards = len(self.cards)
                super().__le__(other)

                def move_card(crd):
                    nonlocal delta
                    crd.x = delta
                    delta += (card_spacing + crd.w)
                    return crd

                if n_cards > 1:
                    all_cards_width = sum(card.w for card in self.cards)
                    all_spacing, card_width = WIDTH - all_cards_width, all_cards_width // n_cards
                    card_spacing = all_spacing // (n_cards + 1)
                    delta = card_spacing
                    [move_card(crd=card) for x, card in enumerate(self.cards)]

            def bind(self, ev=None):
                self.foi_evs.append(ev) if ev not in self.foi_evs else None

            def vai(self, ev=NoEv):
                self.marquee("entrando: ")
                super().vai(ev)
                teclemmino.mark(".".join(self.nome.split("zz")[-2:]) if "zz" in self.nome else "@@")
                # teclemmino.mark(".".join(self.nome.split("zz")[-2:]) if isinstance(self.nome, str) else "@@")
                LG.log(4, "CenaSprite vai", self.nome, teclemmino.vito.INV.cena.nome)
                [foi(ev) for foi in self.foi_evs if callable(foi)]
                ...

            def __call__(self, *args, **kwargs):
                return self

            def parse(self, ref, *_):
                _ = self
                return teclemmino.assets[f"{ref}"]

        class SpriteLabirinto:
            def __init__(self, img, index=(), local=(), **kwargs):
                # from random import sample
                self.local = local
                dx, dy = self.index = Dim(*index)
                xdx = dx + 2
                all_images = list(range(32))
                all_images = all_images * 8
                _blank = ([""]*4) * dx * dy
                _locais = list(local) + _blank
                # _index = enumerate([sample(all_images, 4)  for _ in range(dx*dy)])
                _index = enumerate(zip([all_images[ix * 4:ix * 4 + 4] for ix in range(dx * dy)], _locais))
                # self.salas = salas if salas else self.build_rooms
                self.nome = _name = kwargs["nome"]
                self.salas = _salas = [
                    teclemmino.sprite_sala(f"{_name}zz{ii}", img=img, local=lc, index=ix)
                    for ii, (ix, lc) in _index]
                self.matrix: List[SpriteSala]
                self.matrix = [None] * xdx
                _matrix = [[None] + _salas[ix:ix + self.index.dx] + [None] for ix in range(0, dx * dy, dx)] + [
                    [None] * xdx]
                _ = [self.matrix.extend(row) for row in _matrix]
                LG.log(4, "SpriteLabirinto", local, _salas[0].norte.local)
                self.lb()

            def vai(self, *_):
                self.salas[0].norte.vai()

            def get(self, jj, kk=-1):
                result = f"{self.nome}zz{jj}" if kk < 0 else f"{self.nome}zz{jj}zz{kk}"
                return teclemmino.assets[result]

            # noinspection PyUnresolvedReferences
            def lb(self):
                dx, dy = self.index
                xdx = dx + 2
                winds = [-xdx, 1, xdx, -1]
                for index_sala in range(xdx + 1, xdx + xdx * dy - 1):
                    for wind, winder in enumerate(winds):
                        LG.log(3, "for wind, winder ", index_sala + winder, len(self.matrix))
                        origin, destination = self.matrix[index_sala], self.matrix[index_sala + winder]
                        if origin and destination:
                            origin.cenas[wind].portal(N=destination.cenas[wind])
                            counter_wind = (wind + 2) % 4
                            destination.cenas[counter_wind].portal(N=origin.cenas[counter_wind])

        class SpriteSala(vito.Salao):
            def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, img=None, index=(), local=(), sid=None, **kwargs):
                # _salas = [vito.CenaSprite(img, ix) for ix in index]
                _name = kwargs["nome"]
                _salas_ = enumerate(zip(index, list(local) + [""] * 4))
                _salas = [
                    teclemmino.cena(f"{_name}zz{ii}", img=img, local=lc, index=ix) for ii, (ix, lc) in _salas_]

                self.cenas = _salas if _salas else [n, l, s, o]
                self.nome, self.local = sid, local
                _ = kwargs
                self.p()

                LG.log(4, sid, kwargs, _salas, self.norte, teclemmino.assets)

            def vai(self, *_):
                self.norte.vai()

            def parse(self, ref, ix, *_):
                _ = self
                return teclemmino.assets[f"{ref}zz{ix}"]

        class Texto:
            DOIT = True
            modal = None

            def __init__(self, tit="", txt="", cena=NADA, foi=None, nome=None, pr=-1, **kwargs):

                class TextModal:
                    def __init__(self):
                        self.answer = None
                        self.radios = []
                        self.textual, self.questions = tit, kwargs
                        self.engage = self.dismiss = self.close = lambda *_: None
                        self.modal, self.texter = self.dom("aaa", "bbb")
                        LG.log(4, "Teclemmino ⇒ TextModal__init__ ", super_text.kwargs, super_text.question)

                        _ = teclemmino.vito.document <= self.modal

                    def bind(self, e, d, c, t, q, a):
                        self.engage, self.dismiss, self.close = e, d, c
                        self.textual, self.questions, self.answer = t, q, a
                        LG.log(4, "Teclemmino ⇒ TextModal bind", t, q, a, super_text.kwargs)

                    def unbind(self):
                        self.engage = self.dismiss = self.close = lambda *_: None

                    def option(self, _txt):
                        rd, qu, ct, fi, it = "radio question control field is-info".split()
                        d, f, a, i, s, h, h1 = list(teclemmino.tag_one)
                        p, b, hd, sc, fm, fs, ip, lg, lb, ft = list(teclemmino.tag_two)
                        if _txt:
                            k, v = _txt.pop(0)
                        else:
                            return ""
                        circled = {k: v for k, v in zip(A2J, "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿ")}
                        res = d(d(lb(i_rad := ip(id=f"_radio_{k}", type=rd, name=qu), Class=rd) +
                                  f"\n{circled[k]} {v}", Class=ct), Class=fi)
                        self.radios.append(i_rad)
                        return res + self.option(_txt) if _txt else res

                    def dom(self, exi=None, mod=None):

                        d, f, a, i, s, h, h1 = list(teclemmino.tag_one)
                        p, b, hd, sc, fm, fs, ip, lg, lb, ft = list(teclemmino.tag_two)
                        ii, iw, ig = "button is-info", "button is-warning", "button mr-0 is-danger"
                        eng, dis, clo = "modal_eng modal_dis modal_clo".split()
                        card = d(
                            d(hd(p("A V A N T A R 🐧", Class="modal-card-title") +
                                 (closer := b(Class="delete", id=exi, ariaLabel="close")), Class="modal-card-head") +
                              sc(d(fm(
                                  fs(texter := lg(self.get_text())),
                                  Class="form-horizontal"), Class="content"), Class="modal-card-body") +
                              # ft((eng := b("Entrar Aqui", Class=ii, id=eng)), Class="modal-card-foot"), "modal-card"),
                              ft(
                                  d(d(engage := b("Entrar Aqui", Class=ii, id=eng), Class="control") +
                                    d(disengage := b("Cancela", Class=ig, id=dis), Class="control"),
                                    Class="field is-grouped"), Class="modal-card-foot mb-5"),
                              Class="modal-card"),
                            Class="modal", id=mod)
                        closer.bind("click", self.close_modal)
                        disengage.bind("click", self.close_modal)
                        engage.bind("click", self.engage_modal)
                        # cancel.bind("click", self.cancel_modal)
                        return card, texter

                    def template_modal(self, ev, template=None):
                        ev.stopPropagation()
                        ev.preventDefault()
                        template = teclemmino.parser(template)
                        LG.log(5, "Teclemmino lModal ⇒ template_modal", template)
                        template()
                        self.unbind()
                        self.modal.classList.remove('is-active')

                    def get_text(self):
                        return self.textual

                    def close_modal(self, ev):
                        self.template_modal(ev, template=self.close)

                    def engage_modal(self, ev):
                        ok = [rd.checked for rd in self.radios if rd.id[-1] == self.answer] if self.questions else [
                            True]
                        na = [(rd.checked, rd.id[-1]) for rd in self.radios]
                        LG.log(4, "Teclemmino lModal ⇒ engage_modal", na, self.questions, self.answer, ok)
                        self.template_modal(ev, template=(self.engage if ok[-1] else self.dismiss))

                    def cancel_modal(self, ev):
                        self.template_modal(ev, template=self.dismiss)

                    def mostra(self):  # , tit="", txt="", act=None, **kwargs):
                        modal = teclemmino.vito.document["bbb"]
                        modal.classList.add('is-active')
                        self.modal.classList.add('is-active')
                        self.texter.text = self.textual
                        options = self.option(self.questions[:])
                        _ = (self.texter <= options) if options else None
                        LG.log(5, "Teclemmino Modal ⇒ mostra", self.textual, self.questions, self.answer, kwargs)

                self.cena = cena
                cena.bind(self.vai_vai) if hasattr(cena, "bind") else None
                self.pr = pr
                super_text = self
                self.kwargs = [(k, v) for k, v in kwargs.items()]
                self.question = sorted(list({k: v for k, v in kwargs.items() if k in A2J}.items()))
                self.answer = kwargs["Z"] if "Z" in kwargs else False

                self.esconder = foi if foi else self.nop
                self.tit, self.txt, self.nome = tit, txt, nome
                LG.log(4, "Teclemmino ⇒ Texto", kwargs, self.tit, self.txt, self.nome, self.question, foi)
                self.modal = Texto.modal if Texto.modal else TextModal()
                Texto.modal = self.modal  # dom("modal_closer_", "modal_popup_")
                # self.deploy()

            def nop(self):
                pass

            def parse(self, nome, *args):
                _ = self
                puz = teclemmino.assets[nome]
                LG.log(5, "Texto parse", nome, puz, *args)
                return puz.cena

            def vai_vai(self, ev=NoEv):
                LG.log(5, " Modal ⇒ vai_vai", self.cena.nome, teclemmino.vito.INV.cena.nome, ev)
                self.vai()  # if self.cena == teclemmino.vito.INV.cena else None
                # self.mostra()

            def deploy(self, *_):
                pass

            def esconde(self):
                LG.log(5, "Teclemmino ⇒ Texto esconde", self.esconder, callable(self.esconder) and self.esconder())
                self.esconder.vai() if hasattr(self.esconder, "vai") else None
                # noinspection PyTypeChecker
                _vai = self.esconder() if callable(self.esconder) else teclemmino.parser(self.esconder)
                #
                _vai.vai() if hasattr(_vai, "vai") else None
                teclemmino.premiar(self.pr, vito=vito, tit=self.txt) if self.pr >= 0 else None
                pass

            def mostra(self):  # , tit="", txt="", act=None, **kwargs):
                self.modal.bind(self.esconde, self.nop, self.nop, self.tit, self.question, self.answer)
                self.modal.mostra()  # classList.add('is-active')
                LG.log(5, "Teclemmino Texto ⇒ mostra", self.question, self.tit)

            def vai(self, ev=NoEv()):
                ev.stopPropagation()
                ev.stopPropagation()
                self.mostra()  # self.tit, self.txt, act=self.esconde)
                return False

        class Puzzle(Sprite):
            def __init__(self, img="", x=100, y=100, w=900, h=500, foi="", pr=-1, dif=0.02, **kwargs):
                self.pr = pr
                self.cena, self.nome = lambda: None, None
                swap = self
                foi = self.prepare(foi, kwargs)
                cena = self.cena
                img_, _style, _dim = [v for v in img.values()] if isinstance(img, dict) else (img, {}, D11)
                dim = kwargs["dim"] if "dim" in kwargs else [_dim.dx, _dim.dy]
                dw, dh = dim
                LG.log(4, f"Puzzle(Sprite) foi {foi()}:", cena, cena() if callable(cena) else "#", foi, dim, dw, dh)
                super().__init__(img="", x=x, y=y, w=w, h=h, foi=foi, **kwargs)

                class Peca(vito.Elemento):
                    def __init__(self, local, index):
                        self.local, self.index = local, index,

                        pw, ph = w // dw, h // dh
                        """largura e altura da peça"""
                        lx, ly = x + local % dw * pw, y + local // dw * ph
                        """posição horizontal e vertical em pixels onde a peça será desenhada"""
                        px, py = index % dw * pw, index // dw * ph
                        """posição horizontal e vertical em pixels onde o desenho da peça está na imagem"""
                        super().__init__(img_, x=lx, y=ly, w=pw, h=ph, drag=True, cena=cena())  # , **kwargs)
                        """chama o construtor do Elemento Vitollino passando as informações necessárias"""
                        self.siz = (w, h)
                        """redimensiona a figura da imagem para o tamanho fornecido"""
                        self.elt.id = f"_swap_{local}"
                        """rotula o elemento da peça com a posição onde foi alocada"""
                        self.pos = (-px, -py)
                        """reposiciona a figura da imagem para o pedaço que vai aparecer na peça"""
                        self.elt.ondrop = lambda ev: self.drop(ev)
                        """captura o evento drop da peça para ser tratado pelo método self.drop"""

                    def drop(self, ev):
                        ev.preventDefault()
                        ev.stopPropagation()
                        src_id = ev.data['text']
                        local = int(src_id.split('_')[-1])
                        LG.log(4, f"local -> {local}: {src_id}| índice -> {self.index}")
                        self.dropped(local)

                    def dropped(self, local):
                        # o_outro = swap.pecas[local].pra_la(self, self.x, self.y, local)
                        # o_local = swap.pecas[local].local
                        m, u = self, swap.pecas[local]
                        u.x, u.y, u.local, m.x, m.y, m.local = m.x, m.y, m.local, u.x, u.y, u.local
                        LG.log(4, f"índice, o outro -> {self.index} @ {self.local} <-> {u} @ {u.local}")
                        swap.montou()

                    def certo(self):
                        return self.index == self.local

                    def __repr__(self):
                        return str(self.index)

                from random import shuffle
                pecas = list(range(dw * dh))
                # pecas = list(range(_dim.dx * _dim.dy))
                shuffle(pecas)
                # Peca(0, 0)
                self.pecas = [Peca(local, index) for local, index in enumerate(pecas)] if dim else []
                self.diff = teclemmino.vito_weather_overlay(vito, cena, dif)

            def prepare(self, foi, kwargs):
                cena = kwargs["cena"]
                self.cena = kwargs["cena"] = (
                    CenaSprite(img=cena, direita=foi) if "dim" in kwargs else cena)
                self.cena.nome = self.nome = str(foi)
                return teclemmino.parser(foi)

            def parse(self, nome, *args):
                _ = self
                puz = teclemmino.assets[nome]
                LG.log(5, "Puzzle parse", nome, puz, *args)
                return puz.cena

            def limpa(self):
                [peca.elt.remove() for peca in self.pecas]

            def montou(self):
                # self.current_difficulty += self.dif
                # self.weather.o = self.current_difficulty
                self.diff.dif()
                resultado = all([peca.certo() for peca in self.pecas])
                LG.log(4, resultado)
                self.vai() if resultado else None
                teclemmino.premiar(self.pr, vito, tit=self.tit) if resultado and self.pr >= 0 else None
                return resultado

        class Cube(Puzzle):
            def __init__(self, img="", x=100, y=100, w=900, h=600, foi="", pr=-1, dif=0.01, **kwargs):
                self.pr = pr
                # c = kwargs["cena"]
                # c.nome = str(img)
                # self.cena, self.nome = lambda: None, None
                # foi = self.prepare(foi, kwargs)
                dim, kwargs["dim"] = kwargs["dim"], (0, 0)
                super().__init__(img=img, x=x, y=y, w=w, h=h, foi=foi, pr=pr, dif=dif, **kwargs)
                cenas = CUBE_SIDES
                cenas = img.split() if img else cenas
                dmx, dmy = dim  # kwargs["dim"] if "dim" in kwargs else [3, 2]

                self.cb = vito.Cubos(cenas, cena=self.cena, tw=w, th=h, nx=dmx, ny=dmy, foi=self.montou)
                self.diff.entra(self.cena)
                # _ = self.cena.elt <= self.diff.elt
                # self.go = self.cb.go
                self.cb.go = self.roll
                # self.diff = teclemmino.vito_weather_overlay(vito, self.cena, dif)
                LG.log(4, "Vito ⇒ Cubo deploy⇒", self.pr, self.diff.img, self.cena, self.cena)

            def roll(self):
                self.diff.dif()
                # print("roll", self.diff.current_difficulty)
                # self.go()

            def montou(self):
                # resultado = all([peca.certo() for peca in self.pecas])
                # print(resultado)
                LG.log(4, "Vito ⇒ Cubo montou⇒", self.pr, self.tit)
                self.vai()
                teclemmino.premiar(self.pr, vito, tit=self.tit)
                return True

        class Thrash(Sprite):
            def __init__(self, img="", x=0, y=30, w=1300, h=650, foi="", pr=-1, dif=0.05, **kwargs):
                # noinspection SpellCheckingInspection
                self.sujeira = ['sujeira', 'blob', 'sujo', 'formiga', 'areia', 'casca', 'papel', 'copinho',
                                'aranha', 'latinha'] * 4
                self.pr = pr
                self.cena = self.fundo = self.remaining_shuffle_count = self.rubbish = self.nome = None
                foi = self.prepare(foi, kwargs)
                super().__init__(img=img or RUBBISH, x=x, y=y, w=w, h=h, foi=foi, pr=pr, dif=dif, **kwargs)
                LG.log(4, "Vito ⇒ Thrash __init__⇒", self.pr, foi, self.img_, img, kwargs)
                self._inicia()
                self.diff = teclemmino.vito_weather_overlay(vito, self.cena, dif)

            def prepare(self, foi, kwargs):
                cena = kwargs["cena"]
                self.cena = kwargs["cena"] = (
                    CenaSprite(img=cena, direita=foi) if "dim" in kwargs else cena)
                self.cena.nome = self.nome = str(foi)
                return teclemmino.parser(foi)

            def _inicia(self, *_):

                self.cache = self.create_script_tag(LIXO)
                self.bonus = 20
                # pycard = vito.document["pydiv"]
                pycard = vito.document.body
                hidden = vito.Elemento('', style={'position': 'absolute', 'top': -2000, 'left': -2000})
                _ = hidden.elt <= self.cache
                _ = pycard <= hidden.elt
                self.comida = ['carpa', 'bacalhau', 'atum', 'robalo', 'dourado']
                self.dump(self.cena)

            def __vai(self, *_):
                _ = self
                self.dump(self.cena)

            def parse(self, nome, *args):
                _ = self
                puz = teclemmino.assets[nome]
                LG.log(5, "Puzzle parse", nome, puz, *args)
                return puz.cena

            def dump(self, cena, sorte=4):
                from random import shuffle, randint
                h = Hero(1, 2, 10)  # TheHero()
                self.cena = cena
                self.remaining_shuffle_count = 20 + 2 * h.pers + h.level // 5
                self.rubbish = vito.svg.svg(version="1.1", viewBox="400 250 1000 600", width="1600", height="800")
                _ = self.elt <= self.rubbish
                comer = self.comida * (4 + h.level // 2)
                shuffle(comer)
                shuffle(lixo)
                trash = 20 + 2 * h.level
                sujo = 10 + 2 * h.level
                sorte += h.luck + randint(0, h.level) // 3
                pilha = lixo[:trash] + self.sujeira[:sujo] + comer[:sorte] + ['gato']
                shuffle(pilha)
                # noinspection SpellCheckingInspection
                for indice, label in enumerate(pilha):
                    dx, dy = randint(-300, 300), 100 - randint(-100, 100)
                    dy = (300 - abs(dx)) // 2
                    dx, dy = 200 - dx, 100 - randint(-dy, dy)
                    obj = vito.svg.use(
                        id=f"#{indice:03d}{label}", href=f"#{label}", x=200, y=100, width=250, height=250,
                        transform=f"translate({dx} {dy})  rotate({7 * indice} {R_OFF_X} {R_OFF_Y}) scale(2.5)")
                    _ = self.rubbish <= obj
                    obj.bind('click', self._vai)
                    obj.setAttribute("data-didit", "_no_")

            # def _vai_(self, ev):
            #     self.__vai(ev)

            def quit(self, *_):
                self.remaining_shuffle_count = 0
                if not self.remaining_shuffle_count:
                    self.fundo.elt.remove()
                    # self.desiste.elt.remove()
                    # TheHero().learn(self.bonus)
                    return

            def _vai(self, ev):
                from random import randint
                ev.preventDefault()
                ev.stopPropagation()
                self.diff.dif()
                self.remaining_shuffle_count -= 1
                if not self.remaining_shuffle_count:
                    self.quit()
                    return

                dx, dy = randint(-300, 300), 100 - randint(-100, 100)
                dy = abs(300 - dx) // 3
                dx, dy = 200 - dx, 100 - randint(-dy, dy)
                obj = vito.document[ev.target.id]
                obj_name = ev.target.id[4:]
                if obj.getAttribute("data-didit") == "_did_":
                    return
                if obj_name in self.comida + ["gato"]:
                    food = vito.Elemento('', x=0, y=50, w=200, h=200, tit=f"{ev.target.id}_", cena=self.cena)
                    stag = vito.svg.svg(version="1.1", width="200", height="200")
                    _ = food.elt <= stag
                    _ = stag <= obj
                    obj.setAttribute('transform', f"translate(-{R_OFF_X - 485} -{R_OFF_Y - 170}) scale(0.60 1.35)")
                    # obj.setAttribute('transform', f"translate(-{R_OFF_X - 485} -{R_OFF_Y - 220}) scale(0.60 1.35)")
                    vito.INV.bota(food)
                    obj.setAttribute("data-didit", "_did_")
                    if obj_name == "gato":
                        obj.setAttribute('transform', f"translate(-{R_OFF_X - 485} -{R_OFF_Y - 295}) scale(0.60 0.6)")
                        # food.vai = TheHero().calma
                        # TheHero().blacking(food.tit)
                        return
                    # TheHero().fishing(food.tit)
                else:
                    obj.setAttribute(
                        'transform',
                        f"translate({dx} {dy})  rotate({7 * randint(0, 70)} {R_OFF_X} {R_OFF_Y}) scale(2.5)")

            @staticmethod
            def create_script_tag(src):
                import urllib.request
                _fp = urllib.request.urlopen(src)
                _data = _fp.read()

                _tag = vito.document.createElement('div')
                _tag.html = _data
                return _tag

        class Quiz:
            def __init__(self, nome=None, **kwargs):
                self.quiz = kwargs
                self.nome = nome

        class Mapa:
            def __init__(self, nome=None, **kwargs):
                def deploy(actor, local=(0, 0), **kwa):
                    _kwa = actor.copy()
                    local_ = mapa.get(*local)
                    _kwa.update(kwa)
                    kwa_ = dict(x=kwa["x"] if "x" in kwa else 100, y=100)
                    _kwa.update(**kwa_)
                    _kwa.update(**dict(img=self.parser(kwa["img"]))) if "img" in kwa else None
                    txt = _kwa["texto"] if "texto" in _kwa else {}

                    LG.log(4, "Vito ⇒ Mapa deploy⇒", txt, _kwa["img"] if "img" in _kwa else 9999)
                    # LG.log(4, "Vito ⇒ Mapa deploy⇒", actor.img_, type(txt), local, local_, _kwa)
                    sprite = Sprite(cena=local_, **_kwa)
                    # sprite.o = 0.5
                    return sprite

                self.mapa = mapa = teclemmino.assets[nome]
                self.nome = nome
                pool = 'bio atm xpr cli fri geo per enc sup des res cai jor kpa'.split()
                act_pool = {k[0]: teclemmino.assets[f"m{k}"] for k in pool}
                act_pool["w"] = teclemmino.assets["mcli"]
                LG.log(4, "Vito ⇒ Mapa ⇒", nome, mapa, kwargs)
                self.acts = [deploy(act_pool[key.lower()[0]], **ka) for key, ka in kwargs.items()]

            def get(self, room, side):
                return teclemmino.assets[f"{self.nome}zz{room}zz{side}"]

            def vai(self, *_):
                self.mapa.vai()

            def parser(self, ref: str):
                _ = self
                if isinstance(ref, str) and ref.startswith("."):
                    _, _, repo, folha, ix, *_ = ref.split(".")
                    LG.log(4, "Vito ⇒ Mapa parser⇒", repo, folha, ix, teclemmino.assets[repo][folha].get_image(ix))
                    return teclemmino.assets[repo][folha].get_image(ix)
                else:
                    return ref

        self.vito = vito
        self.rosa = self.avt = self.editor = None
        self.assets = {}
        self.last = {}
        self.classes = (CenaSprite, Sprite, SpriteSala, Texto, Folha, SpriteLabirinto, Mapa, Puzzle, Quiz, Cube, Thrash)
        self.cmd = self.vito_element_builder(vito, self.classes)

    def parser(self, ref: str):
        if isinstance(ref, str) and ref.startswith("."):
            _, _, cls, *ix = ref.split(".")
            return self.assets[cls].parse(cls, *ix)
        else:
            return ref

    def vito_weather_overlay(self, v, cena, dif, img=None):
        class Weather(v.Elemento):
            def __init__(self):
                from random import choice

                # noinspection SpellCheckingInspection
                clim = img or choice("mpOU7Ca tGXhkjw i5dLK8G4 4B1xuMw 9iGTJ6Q OlOj4FV".split())
                super().__init__(f"https://i.imgur.com/{clim}.gif", x=0, y=0, o=0.2, w=1350, h=650, cena=cena)
                self.o = 0
                self.current_difficulty = 0
                self.elt.style.pointerEvents = "none"
                self.difficulty = dif

            def dif(self):
                self.current_difficulty += self.difficulty
                self.o = self.current_difficulty

        return Weather()

    def vito_element_builder(self, v, classes):
        (v.CenaSprite, v.Sprite, v.SpriteSala, v.Textor, v.Folha,
         v.SpriteLabirinto, v.Mapa, v.Puzzle, v.Quiz, v.Cube, v.Thrash) = classes
        builder = [self.cena, self.elemento, self.texto, self.sprite_sala, self.folha, self.valor, self.icon,
                   self.sprite_labirinto, self.mapa, self.puzzle, self.cube, self.quiz, self.caixa, self.extra]
        return {k: v for k, v in zip(['c', 'e', 't', 's', 'f', 'v', "i", "l", "m", "p", "u", "q", "r", "x"], builder)}

    def premiar(self, asset, vito, tit="premiado"):
        mdl = vito.Sprite(self.assets["CN"]["_BADGES"].get_image(asset), w=30, h=30, tit=tit, cena=vito.INV.cena)
        vito.INV.bota(mdl)

    def extra(self, asset, **kwargs):
        extra = self

        class Extra:
            def __init__(self, nome=asset):
                self.nome, self.kwargs = nome, kwargs
                self.url = kwargs['url']
                self.foi = kwargs['foi']().vai if "foi" in kwargs else lambda *_: None
                self.cnt = ''
                self.do_vai = self._vai

            def load_from_url(self):
                import urllib.request
                _fp = urllib.request.urlopen(self.url)
                return _fp.read()

            def parse(self, nome, *args):
                self.vai()
                _ = self, nome, *args
                # puz = extra.assets[nome]
                # LG.log(5, "Puzzle parse", nome, puz, *args)
                # return puz.cena

            def _foi(self):
                LG.log(8, "Extra._foi ⇒ ", asset, kwargs)
                self.foi()

            def _vai(self):
                cnt = self.load_from_url()
                LG.log(5, "Extra._vai ⇒ ", asset, kwargs)
                extra.load_(str_io=str(cnt))
                self.foi()

            def vai(self):
                self.do_vai()
                LG.log(5, "Extra.vai ⇒ ", asset, kwargs)
                self.do_vai = self._foi

        url = kwargs['url']  # .replace("@", "_")

        # cnt = load_from_url(url)
        if asset not in self.assets:
            self.assets[asset] = result = Extra(nome=asset)
            LG.log(5, "extra ⇒ ", asset, kwargs, url, result.foi, result.foi())
            result.vai() if "auto" in kwargs else None
        else:
            result = self.assets[asset]
            LG.log(5, "extra ⇒ ", asset, result, url, result.foi, result.foi())
            result.foi()
        return result

        # self.load_(str_io=str(cnt))

    def cena(self, asset, **kwargs):
        self.assets[asset] = result = self.vito.CenaSprite(nome=asset, **kwargs)
        self.last = asset
        LG.log(3, "Vito ⇒ cena", asset, kwargs)
        return result

    def caixa(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        self.assets[asset] = result = self.vito.Thrash(nome=asset, **kwargs)
        return result

    def quiz(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        self.assets[asset] = result = self.vito.Quiz(nome=asset, **kwargs)
        return result

    def puzzle(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        self.assets[asset] = result = self.vito.Puzzle(nome=asset, **kwargs)
        return result

    def cube(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        self.assets[asset] = result = self.vito.Cube(nome=asset, **kwargs)
        return result

    def mapa(self, asset, **kwargs):
        self.assets[asset] = result = self.vito.Mapa(nome=asset, **kwargs)
        return result

    def sprite_labirinto(self, asset, **kwargs):
        self.assets[asset] = self.vito.SpriteLabirinto(nome=asset, **kwargs)
        LG.log(4, "Vito ⇒ sprite_labirinto", asset, kwargs)

    def sprite_sala(self, asset, **kwargs):
        self.assets[asset] = sala = self.vito.SpriteSala(nome=asset, **kwargs)
        # logging.debug("Vito -> cena", asset, kwargs)
        return sala

    def elemento(self, asset, **kwargs):
        # kwargs.update(**asset) if isinstance(asset, dict) else None
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        self.assets[asset] = self.vito.Sprite(nome=asset, **kwargs)

    def texto(self, asset, **kwargs):
        kwargs.update(cena=self.assets[self.last]) if self.last and "cena" not in kwargs else None
        # self.assets[asset] = t = self.vito.Textor(nome=asset, one=self.tag_one, two=self.tag_two, **kwargs)
        self.assets[asset] = t = self.vito.Textor(nome=asset, **kwargs)
        t.deploy(self.vito.document.body)
        LG.log(5, "Vito ⇒ texto", asset, t.kwargs, kwargs)
        # logging.debug("Vito -> texto", asset, kwargs)

    def valor(self, asset, **value):
        self.assets[asset] = dict(**value)
        self.folha(asset, **value) if "*" in str(value) else None
        # print("Vito asset, value, self.assets[asset] -> valor: ", asset, value, self.assets[asset])

    def folha(self, asset, **kwargs):
        img = self.assets[asset]
        for at, fl in kwargs.items():
            img[f"_{at}"] = (self.vito.Folha(img[at], fl, nome=at) if at in img else self.vito.Icon(at))

    def icon(self, asset, item="", index=None):
        self.assets[asset] = self.vito.CenaSprite("") if asset not in self.assets else self.assets[asset]
        element = self.assets[asset][item] if isinstance(self.assets[asset], dict) else lambda at=asset: self.assets[at]
        value = element.get_image(index=index) if hasattr(element, "get_image") else element
        LG.log(4, "icon:->", asset, item, index, value)
        return value

    def parse_(self, toml_obj):
        DOT = "."

        def parse_key(key: str, dot=DOT):
            # print("parse_key key: ->", key)

            def get_parts(key_, sep=SEP):
                tag_, *parts = key_.split(sep)
                # print("parse_key get_parts: ->", key, tag, SEP.join(parts))
                return tag_[0], sep.join(parts)

            if key.startswith(dot):
                """O identificador é uma referência para uma folha de sprite ou um ćine da fonte awesome"""
                key = key[1:]  # remove o ponto inicial
                cmd, name, tag, *index = key.split(dot)
                index = dict(index=index[0]) if index else {}
                result = self.cmd[cmd](name, item=tag, **index)
                # LG.log(4,"parse_key é uma referência: ⇒", cmd, name, index, f">{result}<")

                return result
            else:
                return list(get_parts(key)) if SEP in key else key

        def go(cmd, name, **value_):
            # @@ FIX
            val = {k: parse_key(v) if isinstance(v, str) else v for k, v in value_.items() if SEP not in k}
            # val = {k:v for k,v in value_.items() if SEP not in k}
            LG.log(2, "cmd, name, value,: ⇒", cmd, name, value_, val)
            self.cmd[cmd](name, **val)
            [self.parse_({sub: v}) for sub, v in value_.items() if SEP in sub]  # self.last=name
            # self.last = None

        # toml_it = [key.split(SEP) + [value] for key, value in toml_obj.items() if SEP in key]
        toml_it = [parse_key(key) + [value] for key, value in toml_obj.items() if SEP in key]
        [go(cmd, name, **value) for cmd, name, value in toml_it]
        return True

    def load_(self, cfile=str('view/core/avantar.toml'), str_io=None):
        import tomlib
        # self.splash_screen()
        if str_io:
            self.avt = str_io
            tom_obj = dict(tomlib.loads(self.avt))
            self.parse_(tom_obj)
            self.start_game_from_root_element()
            return True

        with open(cfile, "r") as avt:
            avt.seek(0)
            self.avt = avt.read()
            tom_obj = dict(tomlib.loads(self.avt))
            self.parse_(tom_obj)
            # print("self.assets", self.assets)
        # self.start_game_from_root_element()
        LG.log(4, "load_ ⇒ file_, cfile, str_io,: ⇒", cfile, str_io, "\n", self.avt[:100])
        # self.splash_screen() if not str_io else self.start_game_from_root_element()
        return str_io

    def mark(self, coord):
        self.rosa.elt.text = coord

    def splash_screen(self):
        splash = self.vito.Cena("/image/avantar_splash.jpg")

        splash.vai()
        self.vito.Sprite("*fa fa-play fa-10x", x=800, y=450, w=150, h=150, cena=splash, tit="Vamos Jogar!",
                         vai=self.start_game_from_root_element)
        self.vito.Sprite("*fa fa-circle fa-2x", x=950, y=180, w=60, h=60, o=0.1, cena=splash, tit="*",
                         vai=self.start_toml_editor)
        self.vito.Elemento("https://imgur.com/sxAm5LA.png", x=580, y=440, w=160, h=160, o=0.1, cena=splash,
                           tit="Avantar")

    def start_toml_editor(self, _=None):
        def send_toml_to_loader(*_):
            toml_ = self.editor.getValue()
            self.vito.INV.tira(run.tit)
            self.load_(str_io=toml_)

        cena = self.vito.Cena("", nome="editor").vai()
        run = self.vito.Sprite("*fa fa-play fa-2x", x=800, y=450, w=150, h=150, cena=cena, tit="Salva e Executa",
                               nome="_run_", vai=send_toml_to_loader)
        self.vito.INV.bota(run)
        cena.elt.html = ""
        cena.elt.id = "editor"
        cena.elt.style.minHeight = "650px"
        cena.elt.style.top = "35px"
        # return
        self.editor = editor = self.vito.window.ace.edit("editor")
        editor.setTheme("ace/theme/cobalt")
        editor.session.setMode("ace/mode/toml")
        editor.focus()
        editor.style = dict(position="absolute", top="100px", height="500px")
        editor.style.height = "500px"
        editor.resize()
        editor.setValue(self.avt)

    def manage_code(self):
        window, document, editor, storage = self.vito.window, self.vito.document, self.editor, self.vito.storage
        if "code" in document.query:
            code = document.query.getlist("code")[0]
            editor.setValue(code)
        else:
            if storage is not None and "avantar_toml" in storage:
                editor.setValue(storage["avantar_toml"])
            else:
                editor.setValue(self.avt)
        editor.scrollToRow(0)
        editor.gotoLine(0)

    def start_game_from_root_element(self, _=None):
        self.assets["ROOT"].vai() if "ROOT" in self.assets else None
        self.mark("0.0")


class Main:
    def __init__(self, br):
        # from pathlib import PurePath
        # y = [[l for l in k] for k in x]
        # y= dict(x)
        br.template("_tt_").render(titulo="A V A N T A R 🐧")
        br.template("_version_").render(version=VERSION)
        self.teclemmino = Teclemmino(br)
        self.br = br

    def load(self, cfile=str('avantar.toml')):
        vito, t_e = self.teclemmino.vito, self.teclemmino
        _ = cfile
        t_e.rosa = rosa = vito.Sprite("https://imgur.com/odmJe4Z.jpg", w=30, h=30, o=0.5, cena=vito.INV.cena)
        vito.INV.bota(rosa)

        str_io = self.teclemmino.load_()
        t_e.splash_screen() if not str_io else t_e.start_game_from_root_element()

    def util(self):
        _ = self
        # noinspection SpellCheckingInspection
        alpha = r'!#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        cph = "abc"
        txt = "tests/editor.html"
        print(txt)

        def enc(text, cyp):
            st, cyp = alpha.index(cyp[-1]), cyp[:-1]
            cod = text.translate(str.maketrans(alpha, alpha[st:] + alpha[:st]))
            return cod if not cyp else enc(cod[-1] + cod[:-1], cyp)

        cdd = enc(txt, cph)
        print(cdd)

        def dec(text, cyp):
            st, cyp = alpha.index(cyp[0]), cyp[1:]
            cod = text.translate(str.maketrans(alpha[st:] + alpha[:st], alpha))
            # return cod[off:]+cod[:off] if not cyp else dec(cod[-1]+cod[:-1],cyp)
            return cod if not cyp else dec(cod[:0] + cod[1:], cyp)

        print(dec(cdd, cph))


def main(br):
    Main(br).load()


if __name__ == '__main__':
    unittest.main()
