#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Test Avantar Game with Teclemmino Engine.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.10
        Move from test pager (25).

|   **Open Source Notification:** This file is part of open source program **Labase**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import unittest
from unittest.mock import MagicMock, Mock  # , ANY

from view.core.game import Teclemmino
# noinspection PyProtectedMember
# from view.core.pager import Action, ELEM_ID, LEVEL


class TestTe(unittest.TestCase):
    def setUp(self) -> None:
        # noinspection PyMissingConstructor
        class FakeSubClass(Mock):
            def __init__(self, *args, **kwargs) -> None:
                _ = kwargs, args
                self.did("did")
                pass

            def did(self, a):
                pass

        # print("\nfake init called")
        self.mc = Mock(name="VitoBuildMet", side_effect=FakeSubClass)
        self.mv = MagicMock(name="VitoC")
        self.me = MagicMock(name="VitoE")
        self.mv.Cena = self.mc
        # self.mv.Sprite = self.me
        self.te = Teclemmino(self.mv)

    def test_parse_only(self):
        self.assertTrue(self.te.parse_({"c-a": dict(img="xxx")}))

    def test_parse_cena_element(self):
        toml = {"v_CN": dict(CENA="lets snow"), 'c_base': {
            'img': 'https://i.imgur.com/9M9k6RZ.jpg',
            'e_ping': {
                'img': 'https://i.imgur.com/9M9k6RZ.jpg',
                'x': 10, 'y': 20, 'texto': 'Me parece um animal distante'}}}
        self.do_parse(toml, 3)
        # @@@@ fix self.mc.assert_called_with(nome=ANY, img=ANY)
        self.assertEqual([], self.me.call_args_list)

    def do_parse(self, toml, elements_parsed, cena="CENA"):
        self.assertTrue(self.te.parse_(toml))
        self.assertEqual(elements_parsed, len(self.te.assets))
        # @@@@@ fix self.mc.assert_called()
        self.assertIn("CN", self.te.assets)
        self.assertIn(cena, self.te.assets["CN"])

    def test_parse_cena_reference_d(self):
        toml = dict(
            v_CN=dict(CENA="lets snow"),
            cena_BASE=dict(
                img=".i.CN.CENA"))
        self.do_parse(toml, 2)
        # self.assertIn("CENA", self.te.assets["CN"])
        # @@@@ fix self.mc.assert_called_with(nome=ANY, img="lets snow")
        self.assertEqual([], self.me.call_args_list)

    def test_parse_cena_elm_sprite_d(self):
        toml = dict(
            v_CN=dict(CENA="h://cena.sprite"),
            f_CN=dict(CENA=[4, 4]),
            cena_BASE=dict(
                img=".i.CN._CENA.1"))
        self.do_parse(toml, 2, cena="_CENA")
        self.assertTrue(hasattr(self.te.assets["CN"]["_CENA"], "get_image"))
        # self.mc.assert_called_with(nome=ANY, img='h://cena.sprite')
        # @@@@ fix self.mc.assert_called_with(nome=ANY, img=dict(img_='h://cena.sprite', style_=ANY))
        self.assertEqual([], self.me.call_args_list)

    def test_parse_cena_awesome_icon(self):
        toml = dict(
            v_CN=dict(CENA="h://cena.sprite"),
            f_CN=dict(CENA=[4, 4]),
            cena_BASE=dict(
                img=".i.CN._CENA.1"),
            elemento_PIGU=dict(
                img="*fa fa-gem fa-5x",
                x=700,
                y=300,
                w=64,
                h=64

            )
        )
        self.do_parse(toml, 3, cena="_CENA")
        self.assertIn("_CENA", self.te.assets["CN"])
        self.assertTrue(hasattr(self.te.assets["CN"]["_CENA"], "get_image"))
        # self.mc.assert_called_with(nome=ANY, img='h://cena.sprite')
        # self.mc.assert_called_with(nome=ANY, img=dict(img_='h://cena.sprite', style_=ANY))
        self.assertEqual([], self.me.call_args_list)

    def test_parse_sprite_labirinto(self):
        toml = dict(
            v_CN=dict(CENA="h://cena.sprite"),
            f_CN=dict(CENA=[4, 4]),
            l_ROOT0=dict(img=".i.CN._CENA.0",
                         index=(1, 1),
                         sid="ROOT"
                         ),
            elemento_PIGU=dict(
                img="*fa fa-gem fa-5x",
                x=700,
                y=300,
                w=64,
                h=64

            )
        )
        # print("elf.mc.SpriteLabirinto",self.te.classes[-1], self.te.classes[2])
        self.mv.SpriteLabirinto = self.te.classes[-1]
        self.mv.SpriteSala = self.te.classes[2]
        self.do_parse(toml, 3, cena="_CENA")
        self.assertTrue(hasattr(self.te.assets["CN"]["_CENA"], "get_image"))
        self.assertTrue(hasattr(self.te.assets["ROOT0"], "index"), self.te.assets)
        # self.assertIn("ROOT0zz0", self.te.assets)

    def test_parse_sprite_cena(self):
        toml = dict(
            v_CN=dict(CENA="h://cena.sprite"),
            f_CN=dict(CENA=[4, 4]),
            s_ROOT0=dict(img=".i.CN._CENA.0",
                         index=[0, 1, 2, 3],
                         sid="ROOT"
                         ),
            elemento_PIGU=dict(
                img="*fa fa-gem fa-5x",
                x=700,
                y=300,
                w=64,
                h=64

            )
        )
        mv = MagicMock(name="VitoC")
        mv.Elemento = mv

        class Tc(Teclemmino):
            Folha = mv
            STYLE, NADA, NDCT, NoEv = [mv] * 4
            html = mv
            Elemento, Cena, Salao = [mv] * 3

            def __init__(self, vit):
                super().__init__(vit)

        tc = Tc(mv)

        self.te = Teclemmino(tc)
        self.do_parse(toml, 3, cena="_CENA")
        self.assertIn("ROOT0", self.te.assets)
        self.assertTrue(hasattr(self.te.assets["CN"]["_CENA"], "get_image"))
        # self.mc.assert_called_with(nome=ANY, img='h://cena.sprite')
        # self.mc.assert_called_with(nome=ANY, img=dict(img_='h://cena.sprite', style_=ANY))
        self.assertEqual([], self.me.call_args_list)

    def test_parse_elemento_cena_vai(self):
        toml = dict(
            v_CN=dict(FOI="h://cena.destino", CENA="h://cena.sprite"),
            f_CN=dict(CENA=[4, 4]),
            cena_BASE=dict(
                img=".i.CN._CENA.1",
                elemento_PIGU=dict(
                    img="*fa fa-gem fa-5x",
                    x=700,
                    y=300,
                    w=64,
                    h=64,
                    foi=".i.CN.FOI.1"

                )
            ))
        self.do_parse(toml, 3, cena="_CENA")
        self.assertIn("_CENA", self.te.assets["CN"])
        self.assertTrue(hasattr(self.te.assets["CN"]["_CENA"], "get_image"))
        # self.mc.assert_called_with(nome=ANY, img='h://cena.sprite')
        # self.mc.assert_called_with(nome=ANY, img=dict(img_='h://cena.sprite', style_=ANY))
        self.assertEqual([], self.me.call_args_list)

    def _test_parse_toml(self):
        self.mv.CenaSprite = self.mc
        self.mv.Sprite = self.me
        self.te.start_game_from_root_element = Mock(name="start_game")

        self.assertTrue(self.te.load_('../view/core/avantar.toml'))
        self.assertEqual(11, len(self.te.assets))
        self.mc.assert_called()
        # self.mc.assert_called_with(nome=ANY, img=ANY)
        # self.me.assert_called_with(nome=ANY, img=ANY, x=10, y=20, texto=ANY)
        self.me.assert_called()


if __name__ == '__main__':
    unittest.main()
