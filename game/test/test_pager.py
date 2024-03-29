#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Test client side  UI controller pager.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.09
        add cena, elemento & awesome (failing) (013).
        add testes for Teclemmino (08).

.. versionadded::    23.08
        convert from pager main script (22).
        test card and modal (22a).

|   **Open Source Notification:** This file is part of open source program **Labase**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import unittest
from unittest.mock import MagicMock, Mock, ANY

from view.core.game import Teclemmino
# noinspection PyProtectedMember
from view.core.pager import Action, ELEM_ID, LEVEL


class TestCorePager(unittest.TestCase):
    def setUp(self) -> None:
        class AddMock(MagicMock, dict):
            body = MagicMock(name="doc_body")

            def __add__(self, other):
                return MagicMock(name="doc_add", _value=other)

            def __getitem__(self, item):
                return MagicMock(name="doc_item", _value=item)

            def __le__(self, other):
                return AddMock(name="doc_inc", _value=other)

        magic_doc = AddMock()
        magic_doc.body = AddMock(name="doc_body")

        def binder(_, mck):
            mck.bind = Mock()
            return mck.bind

        # @patch.dict(magic_doc, {"_panel": AddMock(name="doc_item"), "_modal_mod": AddMock(name="doc_mod")})
        def doc_mock():
            # magic_doc.body = AddMock(name="doc_body")
            return Action(magic_doc, _html)

        def html_mock(mocker) -> (MagicMock, dict):
            html_dc = {f: AddMock(name=f"html_{f}") for f in mocker}
            html_ls = [html_dc[key] for key in mocker]
            mh = MagicMock(name="html_mock", return_value=html_ls)
            return mh, html_dc

        ix = [f"_modal_{suf}" for suf in ELEM_ID]
        _html = MagicMock
        dc = {idx: Mock(name=f"dcm_{idx}") for idx in ix}
        _ = {idx: binder(idx, dc[idx]) for idx in ix}
        # magic_doc = AddMock
        # magic_doc["_panel"].html = MagicMock(name="doc_panel")
        t_one, t_two = "d, f, a, i, s, h, h1".split(", "), "p, b, hd, sc, fm, fs, ip, lg, lb, ft".split(", ")
        # magic_doc.__add__ = self._add = MagicMock(name="doc_add")
        # magic_doc.__getitem__.return_value = self._get = MagicMock(name="doc_get")
        _html.DIV, _html.FIGURE, _html.A, _html.IMG, _html.SPAN, _html.H4, _html.H1 = html_mock(t_one)[1].values()
        (_html.P, _html.BUTTON, _html.HEADER, _html.SECTION, _html.FORM,
         _html.FIELDSET, _html.INPUT, _html.LEGEND, _html.LABEL, _html.FOOTER) = html_mock(t_two)[1].values()
        self.am = AddMock
        # magic_doc = {"_panel": AddMock(name="doc_item"), "_modal_mod": AddMock(name="doc_mod")}
        # with patch.dict(magic_doc, {"_panel": AddMock(name="doc_item")}):
        #     self.act = Action(magic_doc, _html)
        self.act = doc_mock()
        self.act.h_one.get_one, self.html_one = html_mock(self.act.h_one.tags_one)
        self.act.h_one.get_two, self.html_two = html_mock(self.act.h_one.tags_two)

    def test_build(self):
        self.act.document["_panel"].__le__ = self.am(name="doc_panel")
        self.act.document.body.__le__ = self.am(name="doc_body_le")
        _ = self.act.build()
        _ = self.html_one["d"]

    def test_create_card(self):
        _ = self.act.create_card(LEVEL["projeto"])
        d = self.html_one["d"]
        self.html_one["f"].assert_called_with(ANY, Class=ANY)
        self.html_one["a"].assert_called_with(ANY)
        img = dict(src='../image/montroig.jpg', style='opacity:0.5; filter:brightness(200%) blur(1px)')
        self.html_one["i"].assert_called_with(**img)
        moc_calls = d.mock_calls

        self.assertEqual(5, len(moc_calls))  # add assertion here
        d.assert_called_with(ANY, Class=ANY)

    def _create_modal(self):
        d = self.html_two["p"]
        b = self.html_two["b"]
        b.assert_called_with(ANY, Class='button is-danger', id='_modal_clo')
        i = self.html_two["ip"]
        i.assert_called_with(id='desc_', name='desc_', type='text', placeholder='descreve o projeto', Class='input')
        self.html_two["fm"].assert_called_once()
        self.html_two["fs"].assert_called_once()
        moc_calls = b.mock_calls
        # print(moc_calls)
        self.assertEqual(6, len(moc_calls))  # add assertion here
        d.assert_called_with(ANY, Class=ANY)

    def test_create_modal(self):
        _ = self.act.create_modal(LEVEL["projeto"], LEVEL["projeto_modal"])
        self._create_modal()

    def test_create_modal_packet(self):
        _ = self.act.create_modal(LEVEL["pacote"], LEVEL["pacote_modal"])
        self._create_modal()

    def test_create_modal_module(self):
        _ = self.act.create_modal(LEVEL["modulo"], LEVEL["modulo_modal"])
        self._create_modal()


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
            l_ROOT0=dict(img =".i.CN._CENA.0",
                            index = (1,1),
                            sid = "ROOT"
                            ),
            elemento_PIGU=dict(
                img="*fa fa-gem fa-5x",
                x=700,
                y=300,
                w=64,
                h=64

            )
        )
        print("elf.mc.SpriteLabirinto",self.te.classes[-1], self.te.classes[2])
        self.mv.SpriteLabirinto = self.te.classes[-1]
        self.mv.SpriteSala = self.te.classes[2]
        self.do_parse(toml, 4, cena="_CENA")
        self.assertTrue(hasattr(self.te.assets["CN"]["_CENA"], "get_image"))
        self.assertTrue(hasattr(self.te.assets["ROOT00"], "index"))
        self.assertIn("ROOT0zz0",self.te.assets)

    def test_parse_sprite_cena(self):
        toml = dict(
            v_CN=dict(CENA="h://cena.sprite"),
            f_CN=dict(CENA=[4, 4]),
            s_ROOT0=dict(img =".i.CN._CENA.0",
                            index = [0,1,2,3],
                            sid = "ROOT"
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
            STYLE, NADA, NDCT, NoEv = [mv]*4
            html = mv
            Elemento, Cena, Salao = [mv]*3
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
            v_CN=dict(FOI="h://cena.destino",CENA="h://cena.sprite"),
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

    def test_parse_toml(self):
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
