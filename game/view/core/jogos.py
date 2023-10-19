#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Vitollino
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Jogos para usar com o Vitollino

    Quebra-cabeças para serem usados na construção de outros jogos.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Classes neste módulo:

    :py:class:`Cubos` Quebra Cabeça com cubos que rolam.

    :py:class:`Roteiro` Facilitador de criação de roteiros.


Changelog
---------
.. versionadded::    22.04
        Criação do módulo de jogos.

.. versionchanged::    22.04.a
        Usa os comandos originais do DOM.

.. versionadded::    22.05
        Criação da classe Roteiro.


.. seealso::

   Documentação geral do SuperPython: `Ajuda do SuperPython`_

.. _`Ajuda do SuperPython`: https://supygirls.readthedocs.io

"""
from vitollino import Cena, Elemento, Texto
from random import randint, sample
# from browser import alert
from collections import namedtuple
Ator = namedtuple('Elenco','ator nome mini alinha')
Fala = namedtuple('Fala','ator fala prox age')  # , defaults=(None,)*4)
A = namedtuple('Ali','e m d')(-1, 0, 1)

IMGUR = "https://i.imgur.com/{}.jpg"
FUNDO = "qWcEao4"
CENAS = "CRNsfXO swVe1IW jiJY1NY GsdFmpz T6pmXbY dJ4WOIh".split()
OFF = 2000
OFX, OFY = 100, 50


class Roteiro:
    def __init__(self, cena, roteiro, elenco=(), foi=None):
        """Cria um roteiro de falas entre diversos personagens.

        Os parâmetros roteiro e elenco são definidos por tupla nomeadas.

            Ator

                ator:
                    instância de elemento do ator que no diálogo.

                nome:
                    nome que vai aparecer no título do ator.

                mini:
                    fração da altura do ator na miniatura (0.1 a 1.0)

                alinha:

        :param cena: cena onde o diálogo acontece.
        :param roteiro: um conjunto de falas entre os personagens.
        :param elenco: caracterização dos personagens.
        :param foi: número de cubos na horizontal.
        """
        self.dic_ator = {a.ator: a for a in elenco}
        _prox = zip(roteiro, roteiro[1:] + [Fala(None, "", None, None)])
        self.foi = foi if foi else lambda *_: None
        roteiro = [Fala(a, f, g if g else (p.ator if p else None), x) for [a, f, g, x], p in _prox]
        self.elenco, self.roteiro = elenco, roteiro
        self._foi = lambda *_: None
        script = self
        for _ator in elenco:
            _ator.ator.vai = self.nada
            _ator.ator.tit = _ator.nome
            _ator.ator.elt.style.filter = "brightness(30%)"
        protagonista = elenco[0].ator if elenco else roteiro[0].ator
        self.atores = [ator.ator for ator in elenco] if elenco else [ator.ator for ator in roteiro]
        protagonista.vai = self.segue
        protagonista.elt.style.filter = "brightness(100%)"

        class Falar(Texto):
            def __init__(self, ator, fala, prox, act=None, mini=1, **kwarg):
                self.ator, self.fala, self.prox = ator, fala, prox
                self._foi = act or self.nada
                minih = 80 / mini
                self.mini = Elemento(ator.img, cena=cena, w=80, h=80, tipo=f"80px {minih}px",
                                     style=dict(top="20%", margin="-10px 10%"))
                super().__init__(cena, fala, **kwarg)

            def esconde(self, *_):
                self.mini.elt.remove()
                self.ator.elt.style.filter = "brightness(30%)"
                script.testa(self.prox)
                # script.segue()
                # super().esconde()
                self._foi()

            def vai(self, *_):
                super().vai()
                self.ator.elt.style.filter = "brightness(5%)"
                self.ator.vai = self.nada

            @property
            def foi(self):
                return self._foi

            @foi.setter
            def foi(self, value):
                self._foi = value

            def nada(self, *_):
                pass

        self._fala = Falar

    def nada(self, *_):
        pass

    def segue(self, *_):
        ator, fala, prox, action = self.scripter()
        # ator.elt.style.filter = "brightness(30%)"
        fala = self._fala(ator, fala, prox, action, mini=self.dic_ator[ator].mini)  # .vai()
        if prox:
            prox.vai = self.segue
        fala.vai()

    def testa(self, prox, *_):
        if self.roteiro:
            prox.elt.style.filter = "brightness(100%)"
        else:
            for ato in self.atores:
                ato.elt.style.filter = "brightness(100%)"

    def scripter(self, *_):
        return self.roteiro.pop(0)

class Sprite:
    def __init__(self, img="", index=1, dx=1, dy=1, w=900, h=500, o=1, b=0, s=1, **kwargs):
        sty = dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter=f"blur({b}px)", scale=s, opacity=o)

        class Img:
            STY = "backgroundPositionX backgroundPositionY backgroundSizeX backgroundSizeY".split()
            def __init__(self, image_index, imx=1, imy=1, imw=900, imh=500):
                self.idx, self.idy, self.imw, self.imh = imx, imy, imw, imh
                self.image_index = image_index
                self.slices = dx*dy
                self.dx = dx

                self.style = {k: f"{v}px" for k, v in zip(self.STY, (0, 0, w, h))}
                self.style.update(**sty)
                self.style.update(backgroundImage=f"url({img})")

            def __getitem__(self, ix):
                gx, gy = ix // self.dx, ix % self.dx
                self.style.update(backgroundPositionX=gx, backgroundPositionY=gy)
                return

            def __iter__(self):
                current_slice = 0
                while current_slice < self.slices:
                    yield self.__getitem__(current_slice)
                    current_slice += 1

        from copy import deepcopy
        self.img_ = deepcopy(img) if isinstance(img, dict) else img
        self.index = index
        self._img = img if hasattr(img,  "upper") else Img(index)
        style_ = {}
        def to_int(key):
            return [int(cdd[:-1]) for cdd in _style[key].split()]

        img_, _style, _dim = [v for v in img.values()] if isinstance(img, dict) else (img, {}, (0,0))
        if _style:
            (ox, oy), (dx, dy) = to_int("backgroundPosition"), to_int("background-size")
            style_["backgroundPosition"] = f"{-ox / 100 * w}px {-oy / 100 * h}px"
            style_["background-size"] = f"{dx / 100 * w}px {dy / 100 * h}px"

        style = dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter=f"blur({b}px)", scale=s)
        style.update(**style_)
        style.update(**{"background-image": f"url({img_})"})
        # noinspection PyCallingNonCallable
    def __getitem__(self, ix):

        return self._img.__getitem__(ix)
    def __iter__(self):
        return self._img.__iter__()


class Cubos:
    CUBOS = None

    def write(self, *_):
        self.foi()

    def __init__(self, cenas, cena=None, tw=None, th=600, nx=4, ny=3, spx=4, spy=3, ofx=OFX, ofy=OFY, foi=None):
        """Jogo que define cubos formando uma cena em cada lado.

        Joga-se clicando em uma das porções cardeais da face do cubo.
        O cubo irá rolar naquela direção.

        :param cenas: Coleção de seis cenas a serem apresentadas.
        :param tw: Tamanho em pixeis de largura da cena.
        :param th: Tamanho em pixeis de altura da cena.
        :param nx: Número de cubos na horizontal.
        :param ny: Número de cubos na vertical.
        :param spx: Colunas do sprite na horizontal.
        :param spy: Linhas do sprite na vertical.
        :param ofx: Deslocamento na horizontal.
        :param ofy: Deslocamento na vertical.
        """

        self.spy, self.spx, self.foi = spy, spx, foi
        _cubos = self

        class Face(Elemento):
            """Representa a face do cubo.

            A face do cubo é sensível ao click em quatro diferentes porções cardeais.
            As porções cardeais são delimitadas pela duas diagonais do cubo.

            """
            def __init__(self, cubo, inx, face, **kwargs):
                """A face pertencente a um cubo do quebra-cabeça.

                :param cubo: O cubo ao qual pertence.
                :param inx: Índice do cubo no quebra-cabeça.
                :param face: Parte do endereço IMGUR da imagem.
                :param kwargs: Parâmetros a serem passados para o elemento 'Vitollino'.
                """
                self.cubo = cubo
                w, h = tw // nx, th // ny
                w = h = min(w, h)
                self.dh = h
                x, y = (inx % nx) * w, (inx // nx) * h
                super().__init__(IMGUR.format(face), x=x + ofx, y=y - OFF + ofy, w=w, h=h,
                                 cena=cena, vai=self.vai,
                                 style={'background-image': "url({})".format(IMGUR.format(face)),
                                        'background-size': f"{tw}px {th}px",
                                        "background-position": f'{-x}px {-y}px'},
                                 **kwargs)
                # self.siz = (tw, th)
                # self.pos = (-x, -y)
                self.yy = y - OFF + ofy
                self.xx = x + OFX
                self.elt.style.width = f"{w}px"
                self.elt.style.height = f"{h}px"
                self.elt.html = ""
                self.quad = 0

            @property
            def xx(self):
                top = self.elt.style.left[:-2]
                return int(top if top else 0)

            @xx.setter
            def xx(self, value):
                self.elt.style.left = "{}px".format(value)

            @property
            def yy(self):
                top = self.elt.style.top[:-2]
                return int(top if top else 0)

            @yy.setter
            def yy(self, value):
                self.elt.style.top = "{}px".format(value)

            def show(self):
                """Mostra esta face do cubo.

                :return: sempre verdadeiro, para indicar que a face está sendo mostrada.
                """
                self.yy += OFF if self.yy < -10 else 0
                return True

            def hide(self):
                """Esconde esta face do cubo.

                :return: sempre falso, para indicar que a face está sendo ocultada.
                """
                self.yy -= OFF if self.yy > 10 else 0
                return False

            def orient(self, ori):
                """ Reorienta a face para refletir as rolagens do cubo.

                :param ori: Quadrante da rotação da face, entre 0 e 3.
                :return: Sempre falso.
                """
                self.elt.style.transform = f"rotate({ori * 90}deg)"
                return False

            def vai(self, evt):
                """Recebe o click na face e calcula qual quadrante cardeal foi clicado.

                Calcula a posição relativa do click na face.
                Determina o click em relação às duas diagonais da face.
                As diagonais são x=-y e x=y+h.

                :param evt: Evento recebido do navegador.
                :return:
                """
                e = evt.target
                dim = e.getBoundingClientRect()
                x = evt.clientX - dim.left
                y = evt.clientY - dim.top
                e, n, h = x - y, x + y, self.dh
                self.quad = 0 if (e > 0) and (n < h) else 1 if (e > 0) and (n > h) else 2 if (e < 0) and (n > h) else 3
                # Cubo.CUBOS.write(f"x: {x} y: {y} qd: {self.quad}")
                self.cubo.go(self.quad)

        class Cubo:
            """Cubo para formar um quebra-cabeças de seis imagens.

            Cada cubo contém um recorte quadrado de cada uma das seis imagens nas suas faces.
            O cubo rola quando se clica na face que esta sendo apresentada (virada para cima).
            Ao rolar, o cubo vai apresentar uma nova face, dada pela direção indicada na rolagem.

            """
            ROLL = [
                [[19, 4, 21, 12], [18, 8, 22, 0], [17, 12, 23, 4], [16, 0, 20, 8], [6, 1, 12, 11], [12, 3, 6, 10]],
                [[5, 22, 13, 16], [9, 23, 1, 19], [13, 20, 5, 18], [1, 21, 9, 17], [2, 13, 8, 7], [0, 7, 10, 13]],
                [[23, 14, 17, 6], [20, 2, 16, 10], [21, 6, 19, 14], [22, 10, 18, 2], [14, 9, 4, 3], [4, 11, 14, 1]],
                [[15, 18, 7, 20], [3, 17, 11, 21], [7, 16, 15, 22], [11, 19, 3, 23], [10, 5, 0, 15], [8, 15, 2, 5]],
            ]
            """Vetor que representa o índice destino da rolagem dado um clique numa face."""

            def __init__(self, inx, faces):
                """Cubo com os recortes das seis imagens nas suas faces.

                :param inx: Índice posicional do cubo no quebra-cabeça, no sentido da leitura.
                :param faces: Lista com as seis imagens que serão apresentadas nas faces do cubo.
                """
                self.faces = [Face(cubo=self, inx=inx, face=face) for face in faces]
                self.face, self.orient = 0, 0

            def roll(self, inx):
                """Rola o dado na direção indicada.

                Caso esta rolagem complete uma das imagens do quebra-cabeça, indica sucesso.

                :param inx: Índice que representa uma combinação da face com a orientação.
                :return: None
                """
                facer, self.orient = inx // 4, inx % 4
                self.face = [face.show() if facer == face_index else face.hide()
                             for face_index, face in enumerate(self.faces)].index(True)
                self.faces[self.face].orient(self.orient)
                Cubo.CUBOS.write("completou com sucesso") if Cubo.CUBOS.complete() else None

            @property
            def inx(self):
                """Índice que representa uma combinação da face com a orientação.

                :return: Índice que representa uma combinação da face com a orientação.
                """
                return self.face * 4 + self.orient

            def go(self, inx):
                go_face_roll = Cubo.ROLL[self.orient][self.face][inx]
                self.roll(go_face_roll)
                _cubos.go()
                # fc1, ot1 = self.face, self.orient
                # Cubo.CUBOS.write(f"inx: {inx} face: {fc0} ori: {ot0} gfr: {go_face_roll} face: {fc1} ori: {ot1} ")

        cena = cena or Cena(IMGUR.format(FUNDO)).vai()
        # tw, th = (tw, tw // nx * ny) if tw else (th // ny * nx, th)
        Cubo.CUBOS = self
        # self.el = Elemento(IMGUR.format(FUNDO), w=300, h=100, cena=cena, style={"color": "white"})
        self.cubos = cubos = [Cubo(inx=inx, faces=cenas) for inx in range(nx * ny)]
        # scrambler = list(range(23)) * (nx*ny//23 + 1)
        scrambler = [ix % 23 for ix, _ in enumerate(cubos)]
        scramble = zip(cubos, sample(scrambler, len(cubos)))
        # [cube.roll(randint(0, 23)) for cube in cubos] * 2
        [cube.roll(face) for cube, face in scramble]
        # [cube.roll(0) for cube in cubos]

    def go(self):
        pass

    def complete(self):
        """Calcula para ver se todos os cubos apresentam a mesma face.

        :return: *True* se todas as faces dos cubos representam a mesma imagem.
        """
        # self.write(set(cubo.inx for cubo in self.cubos))
        return len(set(cubo.inx for cubo in self.cubos)) == 1


if __name__ == "__main__":
    from vitollino import STYLE
    STYLE.update(width=850, height="650px")
    # Cubos(CENAS, tw=500, nx=2, ny=2)
