#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Controls UI page and responds to actions.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.08
        Create new project, package and module (17).
        Gerencia a mudança de nível no cliente (21).
        Registra os três níveis e inicia o datasource (21a).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import uuid
from unittest.mock import patch
from collections import namedtuple
from dataclasses import dataclass
ELEM_ID = "opn eng dis clo exi mod name_ desc_".split()

Level = namedtuple("Level", "title descript name m_dsc m_tit m_nam hpn hpd img")
# ObjectId = namedtuple("ObjectId", ELEM_ID)
ObjectId = namedtuple("ObjectId", "opn eng dis clo exi mod name_ desc_")
TEX0 = dict(descript="Create a new Python project - New Project - Click Here",
            name="Novo Projeto - Clique Aqui",
            title="Novo Projeto",
            m_dsc="Defina seu novo projeto",
            m_nam="Novo Projeto- Clique Aqui",
            m_tit="Descreva seu Novo Projeto",
            hpn="O nome do projeto com uma única palavra minúscula e sem acentos.",
            hpd="Um texto de uma linha descrevendo o projeto.",
            img="../image/montroig.jpg"
            )
TEX1 = dict(descript="Create a new Python packet - New Packet - Click Here",
            name="Novo Pacote - Clique Aqui",
            title="Novo Pacote",
            m_dsc="Defina seu novo pacote",
            m_nam="Novo Pacote - Clique Aqui",
            m_tit="Descreva seu Novo Pacote",
            hpn="O nome do pacote com uma única palavra minúscula e sem acentos.",
            hpd="Um texto de uma linha descrevendo o pacote.",
            img="../image/garden.jpg"
            )
TEX2 = dict(descript="Create a new Python Module - New Module - Click Here",
            name="Novo Módulo - Clique Aqui",
            title="Novo Módulo",
            m_dsc="Defina seu novo Módulo",
            m_nam="Novo Módulo - Clique Aqui",
            m_tit="Descreva seu Novo Módulo",
            hpn="O nome do Módulo com uma única palavra minúscula e sem acentos.",
            hpd="Um texto de uma linha descrevendo o Módulo.",
            img="../image/montroig.jpg"
            )
LEVEL = dict(projeto=Level(**{s: str(t) for s, t in TEX0.items()}),
             pacote=Level(**{s: str(t) for s, t in TEX1.items()}),
             modulo=Level(**{s: str(t) for s, t in TEX2.items()}))
OI = ObjectId(**{suf: str(suf if "_" in suf else f"_modal_{suf}") for suf in ELEM_ID})


class DataSource:
    def __init__(self):
        @dataclass
        class LevelData:
            desc: str
            name: str
            title: str
            pad: str

        self.data_buffer = {}
        self.level = LevelData

    def save(self, desc, name, title, pad=None):
        pad = pad or str(uuid.uuid4().fields[-1])[:9]
        data = self.level(desc, name, title, pad)
        import json
        self.data_buffer[pad] = json.dumps(data)
        return data

    def load(self, pad):
        import json
        data = json.loads(self.data_buffer[pad])
        data = self.level(**data)
        return data

class Action:

    def __init__(self, document, html):
        self.document = document
        level_state = zip("projeto pacote modulo".split(), "pacote modulo projeto".split())
        self.current_level = "projeto"
        self.level = {lvl: nxt for lvl, nxt in level_state}
        self.modal_id = [suf for suf in ELEM_ID]
        self.tags = html.DIV, html.FIGURE, html.A, html.IMG, html.SPAN, html.H4
        self.tagr = (html.P, html.BUTTON, html.HEADER, html.SECTION, html.FORM,
                     html.FIELDSET, html.INPUT, html.LEGEND, html.LABEL, html.FOOTER)
        self.modal = {}
        # self.modal_id = [f"_modal_{suf}" for suf in "opn eng dis clo exi mod pna pde".split()]
        self.bnd = [self.open_modal, self.execute_modal] + [self.close_modal] * 3
    def build(self):
        self.document["_panel"].html = ""
        current_level_text = LEVEL[self.current_level]
        _ = self.document["_panel"] <= self.create_card(current_level_text)
        self.document["_modal_mod"].remove()
        _ = self.document.body <= self.create_modal(current_level_text)
        self.modal = {inx: self.document[tg] for inx, tg in OI._asdict().items()}
        [self.modal[bid].bind("click", handler) for bid, handler in zip(self.modal_id, self.bnd)]

    def open_modal(self, ev):
        ev.stopPropagation()
        ev.preventDefault()
        print("open")
        self.modal["mod"].classList.add('is-active')

    def close_modal(self, ev):
        ev.stopPropagation()
        ev.preventDefault()
        self.modal["mod"].classList.remove('is-active')

    def execute_modal(self, ev):
        ev.stopPropagation()
        ev.preventDefault()
        # print(self.modal[""])
        name, desc = self.modal["name_"].value, self.modal["desc_"].value,
        self.modal["mod"].classList.remove('is-active')
        img = LEVEL[self.current_level].img
        inst = f"Entre no Projeto {name.capitalize()} -Clique Aqui"
        texto = Level(f"Projeto {name.capitalize()}", desc, inst, *(["_NO_"]*5+[img]))
        s = "opacity:0.7; position: absolute; min-width: 400%; min-height: 400%; top=-25%; left=0px;"
        _ = self.document["_panel"] <= self.create_card(texto, s, f"_prj_{name}_")

    def create_card(self, v, style=None, bind_id=None):
        d, f, a, i, s, h = self.tags
        o = bind_id or OI.opn
        img, title, name, descript = v.img, v.title, v.name, v.descript
        style = style or "opacity:0.5; filter:brightness(200%) blur(1px)"
        card = d(
            d(d(f(a(i(src=img, style=style)), Class="image is-4by3 is-clipped"), Class="card-image") +
            d(s(title), Class="card-content is-overlay is-size-1 has-text-weight-bold has-text-black") +
            d(h(name, Class="title is-4"), Class="card-content-header") +
            s(descript)  # , id=m1)
            , Class="card", style="height:100%; overflow:hidden", id=o), Class="column is-4")
        return card

    def create_modal(self, tx):
        def field(_name=ELEM_ID[-2], ph="nomedoprojeto", hlp=""):
            return d(lb(name, For=_name, Class="label") +
                     d(ip(id=_name, name=_name, type="text", placeholder=ph, Class="input") +
                       p(hlp, Class="help"), Class="control"))

        d, f, a, i, s, h = self.tags
        p, b, hd, sc, fm, fs, ip, lg, lb, ft = self.tagr
        mod, opn, eng, dis, clo, exi = OI.mod, OI.opn, OI.eng, OI.dis, OI.clo, OI.exi
        # tx = LEVEL[level]
        # md, me, md, mc, mx, m5, m6, m7 = [f'_modal_{_ix}' for _ix in range(7)]
        # md, mo, me, md, mc, mx, m5 = self.modal_id
        # descript = "Defina seu novo projeto"
        # name = "Novo Project - Clique Aqui"
        # title = "Novo Projeto"
        # hpr = "O nome do projeto com uma única palavra minúscula e sem acentos."
        # hpd = "Um texto de uma linha descrevendo o projeto."
        descript = tx.m_tit
        name = tx.name
        title = tx.title
        hpn, hpd = tx.hpn, tx.hpd
        ii, ig = "button is-info", "button is-danger"
        card = d(
            d(hd(p(descript, Class="modal-card-title") +
                 b(Class="delete", id=exi, ariaLabel="close"), Class="modal-card-head") +
            sc(d(fm(
                fs(lg(title) + field(hlp=hpn) + field(_name=ELEM_ID[-1], hlp=hpd, ph="descreve o projeto")),
                Class="form-horizontal"), Class="content"), Class="modal-card-body") +
            ft(b("Enviar", Class=ii, id=eng) + b("Cancelar", Class=ii, id=dis) +
               b("Fechar", Class=ig, id=clo), Class="modal-card-foot"), Class="modal-card"),
            Class="modal", id=mod)
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
    ixx = ("_modal", "_modal_go", "_close_top", "_close_btn", "_dismiss",
          "_engage", "_proj_desc", "_projeto_desc")
    ix = [f"_modal_{suf}" for suf in "mod opn eng dis clo exi pna pde".split()]
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
    m = act.create_modal(LEVEL["projeto"])
    cd = act.create_card(LEVEL["projeto"])
    # _html.DIV.DIV.assert_any_call()
    print(_add.mock_calls)
    print(_html.DIV.mock_calls)
    print(_html.BUTTON.mock_calls)
    print(" ".join(ELEM_ID))
    print(OI._asdict())
    print()
    #assert act.modal_btn == dc[ix[1]], (act.modal_btn, dc[ix[1]])
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
