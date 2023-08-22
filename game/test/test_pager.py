#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Test client side  UI controller pager.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
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
# noinspection PyProtectedMember
from view._core.pager import Action, ELEM_ID, LEVEL


class TestCorePager(unittest.TestCase):
    def setUp(self) -> None:
        class AddMock(Mock):
            def __add__(self, other):
                return MagicMock(name="doc_add", _value=other)
        def binder(_, mck):
            mck.bind = Mock()
            return mck.bind
        def html_mock(mocker)-> (MagicMock, dict):
            html_dc = {f: AddMock(name=f"html_{f}") for f in mocker}
            html_ls = [html_dc[key] for key in mocker]
            mh = MagicMock(name="html_mock", return_value = html_ls)
            return mh, html_dc
        ix = [f"_modal_{suf}" for suf in ELEM_ID]
        _html = MagicMock
        dc = {idx: Mock(name=f"dcm_{idx}") for idx in ix}
        _ = {idx:binder(idx, dc[idx]) for idx in ix}
        magic_doc = MagicMock
        t_one, t_two = "d, f, a, i, s, h".split(", "), "p, b, hd, sc, fm, fs, ip, lg, lb, ft".split(", ")
        magic_doc.__add__ = self._add = MagicMock(name="doc_add")
        _html.DIV, _html.FIGURE, _html.A, _html.IMG, _html.SPAN, _html.H4 = html_mock(t_one)[1].values()
        (_html.P, _html.BUTTON, _html.HEADER, _html.SECTION, _html.FORM,
        _html.FIELDSET, _html.INPUT, _html.LEGEND, _html.LABEL, _html.FOOTER) = html_mock(t_two)[1].values()
        self.am =AddMock
        self.act = Action(magic_doc, _html)
        self.act.h_one.get_one, self.html_one = html_mock(self.act.h_one.tags_one)
        self.act.h_one.get_two, self.html_two = html_mock(self.act.h_one.tags_two)
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
    def test_create_modal(self):
        _ = self.act.create_modal(LEVEL["projeto"])
        d = self.html_two["p"]
        b = self.html_two["b"]
        b.assert_called_with(ANY, Class='button is-danger', id='_modal_clo')
        i = self.html_two["ip"]
        i.assert_called_with(id='desc_', name='desc_', type='text', placeholder='descreve o projeto', Class='input')
        self.html_two["fm"].assert_called_once()
        self.html_two["fs"].assert_called_once()
        moc_calls = b.mock_calls
        # print(moc_calls)
        self.assertEqual(4, len(moc_calls))  # add assertion here
        d.assert_called_with(ANY, Class=ANY)


if __name__ == '__main__':
    unittest.main()
