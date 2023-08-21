#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Controls UI page and responds to actions.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.08
        Create new project, package and module (17).
        Gerencia a mudança de nível no cliente (21).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from unittest.mock import ANY, patch
from collections import namedtuple

Level = namedtuple("Level", "title descript name m_dsc m_tit m_nam hpn hpd")
TEX0 = dict(descript="Create a new Python project - New Project - Click Here",
            name="Novo Projeto - Clique Aqui",
            title="Novo Projeto",
            m_dsc="Defina seu novo projeto",
            m_nam="Novo Projeto- Clique Aqui",
            m_tit="Novo Projeto",
            hpn="O nome do projeto com uma única palavra minúscula e sem acentos.",
            hpd="Um texto de uma linha descrevendo o projeto."
            )
TEX1 = dict(descript="Create a new Python packet - New Packet - Click Here",
            name="Novo Pacote - Clique Aqui",
            title="Novo Pacote",
            m_dsc="Defina seu novo pacote",
            m_nam="Novo Pacote - Clique Aqui",
            m_tit="Novo Pacote",
            hpn="O nome do pacote com uma única palavra minúscula e sem acentos.",
            hpd="Um texto de uma linha descrevendo o pacote."
            )
TEX2 = dict(descript="Create a new Python Module - New Module - Click Here",
            name="Novo Módulo - Clique Aqui",
            title="Novo Módulo",
            m_dsc="Defina seu novo Módulo",
            m_nam="Novo Módulo - Clique Aqui",
            m_tit="Novo Módulo",
            hpn="O nome do Módulo com uma única palavra minúscula e sem acentos.",
            hpd="Um texto de uma linha descrevendo o Módulo."
            )
LEVEL = dict(projeto=Level(**TEX0), pacote=Level(**TEX1), modulo=Level(**TEX2))

class Action:
    def __init__(self, document, html):
        self.document = document
        self.modal_id = [suf for suf in "mod opn eng dis clo exi pna pde".split()]
        self.tags = html.DIV, html.FIGURE, html.A, html.IMG, html.SPAN, html.H4
        # p, b, hd, sc, fm, fs, ip, lg, lb = self.tagr

        self.tagr = (html.P, html.BUTTON, html.HEADER, html.SECTION, html.FORM,
                     html.FIELDSET, html.INPUT, html.LEGEND, html.LABEL, html.FOOTER)
        self.modal = document["_modal"]
        self.modal_btn = document["_modal_go"]
        self.modal_xxx = document["_close_top"]
        self.modal_nop = document["_close_btn"]
        self.modal_dis = document["_dismiss"]
        self.modal_exe = document["_engage"]
        self.panel_desc = document["_proj_desc"]
        self.modal_desc = document["_projeto_desc"]
        self.modal_btn.bind("click", self.open_modal)
        self.modal_exe.bind("click", self.execute_modal)
        self.modal_xxx.bind("click", self.close_modal)
        self.modal_nop.bind("click", self.close_modal)
        self.modal_dis.bind("click", self.close_modal)

    def _init(self):
        md, me, md, mc, mx, m5, m6, m7 = [f'_modal_{ix}' for ix in range(7)]

        self.modal_id = [suf for suf in "mod eng dis clo exi pna pde".split()]
        self.modal = [self.document[f"_modal_{ix}"] for ix in self.modal_id]
        bnd = [self.open_modal, self.execute_modal] + [self.close_modal] * 3
        [self.modal[bid].bind("click", handler) for bid, handler in zip(self.modal_id, bnd)]
        self.document["_modal_mod"].remove()
        _ = self.document.body <= self.create_modal()

    def open_modal(self, ev):
        ev.stopPropagation()
        ev.preventDefault()
        print("open")
        self.modal.classList.add('is-active')

    def close_modal(self, ev):
        ev.stopPropagation()
        ev.preventDefault()
        self.modal.classList.remove('is-active')

    def execute_modal(self, ev):
        ev.stopPropagation()
        ev.preventDefault()
        print(self.modal_desc.value)
        self.panel_desc.html = self.modal_desc.value
        self.modal.classList.remove('is-active')

    def create_card(self):
        d, f, a, i, s, h = self.tags
        md, mo, me, md, mc, mx, m5, m6 = self.modal_id

        image = "../image/montroig.jpg"
        style = "opacity:0.5; filter:brightness(200%) blur(4px)"
        descript = "Create a new Python project - New Project - Click Here"
        name = "Novo Project - Clique Aqui"
        title = "Novo Project"
        card = d(
            d(f(a(i(src=image, style=style)), Class="image is-4by3"), Class="card-image") +
            d(s(title), Class="card-content is-overlay is-size-1 has-text-weight-bold has-text-black") +
            d(h(name, Class="title is-4"), Class="card-content-header") +
            s(descript)  # , id=m1)
            , Class="card", id=mo)
        return card

    def create_modal(self, level="projeto"):
        def field(_name="_name", ph="nomedoprojeto", hlp=""):
            return d(lb(name, For=_name, Class="label") +
                     d(ip(id=_name, name=_name, type="text", placeholder=ph, Class="input") +
                       p(hlp, Class="help"), Class="control"))

        d, f, a, i, s, h = self.tags
        p, b, hd, sc, fm, fs, ip, lg, lb, ft = self.tagr
        tx = LEVEL[level]
        # md, me, md, mc, mx, m5, m6, m7 = [f'_modal_{_ix}' for _ix in range(7)]
        md, mo, me, md, mc, mx, m5, m6 = self.modal_id
        # descript = "Defina seu novo projeto"
        # name = "Novo Project - Clique Aqui"
        # title = "Novo Projeto"
        # hpr = "O nome do projeto com uma única palavra minúscula e sem acentos."
        # hpd = "Um texto de uma linha descrevendo o projeto."
        descript = tx.descript
        name = tx.name
        title = tx.title
        hpn, hpd = tx.hpn, tx.hpd
        ii, ig = "button is-info", "button is-danger"
        card = d(
            d(hd(p(descript, Class="modal-card-title") +
                 b(Class="delete", id=mx, ariaLabel="close"), Class="modal-card-head"), Class="modal-card") +
            sc(d(fm(
                fs(lg(title) + field(hlp=hpn) + field(_name="_desc", hlp=hpd, ph="descreve o projeto")),
                Class="form-horizontal"), Class="content"), Class="modal-card-body") +
            ft(b("Enviar", Class=ii, id=me) + b("Cancelar", Class=ii, id=md) +
               b("Fechar", Class=ig, id=mc), Class="modal-card-foot"),
            Class="modal", id=md)
        return card


if __name__ == '__main__':
    from unittest.mock import MagicMock, Mock
    def binder(ii,mck):
        mck.bind = Mock()
        return mck.bind
    my_btn = Mock()
    @patch.object(Action,"modal_btn", my_btn.btn)
    def action(dic, htm):
        _act = Action(dic, htm)
        assert my_btn.assert_any_call()
        return _act
    ix = ("_modal", "_modal_go", "_close_top", "_close_btn", "_dismiss",
          "_engage", "_proj_desc", "_projeto_desc")
    _html = MagicMock
    dc = {idx: Mock(name=f"dcm_{idx}") for idx in ix}
    mk = {idx:binder(idx, dc[idx]) for idx in ix}
    myMagic = MagicMock
    test_mock = MagicMock
    myMagic.__add__ = _add = MagicMock()
    # myMagic.__new__ = test_mock
    _html.DIV, _html.FIGURE, _html.A, _html.IMG, _html.SPAN, _html.H4 = [myMagic] *6
    # p, b, hd, sc, fm, fs, ip, lg, lb = self.tagr

    _html.P, _html.BUTTON, _html.HEADER, _html.SECTION, _html.FORM = [myMagic] *5
    _html.FIELDSET, _html.INPUT, _html.LEGEND, _html.LABEL, _html.FOOTER = [myMagic] *5

    act = Action(dc, _html)
    m = act.create_modal()
    cd = act.create_card()
    # _html.DIV.DIV.assert_any_call()
    print(_add.mock_calls)
    print(_html.DIV.mock_calls)
    print(_html.BUTTON.mock_calls)
    assert act.modal_btn == dc[ix[1]], (act.modal_btn, dc[ix[1]])
    #mk[ix[1]].bind.assert_called_with()
'''
<div class="modal" id="_modal">
    <div class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">Defina seu novo projeto</p>
            <button class="delete" id="_close_top" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
            <div class="content">
                <form class="form-horizontal">
                    <fieldset>
                        <!-- Form Name -->
                        <legend>Novo Projeto</legend>
                        <!-- Text input-->
                        <div class="field">
                            <label class="label" for="_projeto">Nome do Projeto</label>
                            <div class="control">
                                <input id="_projeto" name="_projeto" type="text" placeholder="nomedoprojeto"
                                       class="input " required="">
                                <p class="help">O nome do projeto com uma única palavra minúscula e sem acentos.</p>
                            </div>
                        </div>
                        <!-- Text input-->
                        <div class="field">
                            <label class="label" for="_projeto_desc">Descrição do Projeto</label>
                            <div class="control">
                                <input id="_projeto_desc" name="_projeto_desc" type="text" placeholder="descreveprojeto"
                                       class="input " required="">
                                <p class="help">Um texto de uma linha descrevendo o projeto.</p>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
        </section>
        <footer class="modal-card-foot">
            <button class="button is-info" id="_engage">Yes</button>
            <button class="button is-info" id="_dismiss">No</button>
            <button class="button is-danger" id="_close_btn">Close</button>
        </footer>
    </div>
</div>

'''
"""
         <div class="card" id="_modal_go">
                    <!-- image for post -->
                    <div class="card-image">
                        <figure class="image is-4by3">
                            <a href="">
                                <img src="../image/novo_projeto.png"
                                     style="opacity:0.5; filter:brightness(200%) blur(4px)"  alt="Novo Projeto">
                            </a>
                        </figure>
                    </div>
                    <!-- end of image for post -->
                       <div class="card-content is-overlay is-size-1 has-text-weight-bold has-text-black">
                            <span>Novo Projeto</span>
                            <!-- some content to be placed over the image -->
                        </div>

                    <!-- post header -->
                    <div class="card-content-header">
                        <h4 class="title is-4"><a href="">Novo Projeto - Clique Aqui</a></h4>
                    </div>
                    <!-- end of post header -->
                    <span id="_proj_desc">Create a new Python project - New Project - Click Here</span>
                    <!-- post content -->
                </div>
       
"""
