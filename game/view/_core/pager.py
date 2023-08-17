#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""Controls UI page and responds to actions.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.08
        Create new project, package and module (17).

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from unittest.mock import ANY


class Action:
    def __init__(self, document, html):
        self.tags = html.DIV, html.FIGURE, html.A, html.IMG, html.SPAN, html.H4
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
        style = "opacity:0.5; filter:brightness(200%) blur(4px)"
        card = d(
            d(f(a(i(src="../image/novo_projeto.png", style=style)), Class="image is-4by3"), Class="card-image")+
            d(s(), Class="card-content is-overlay is-size-1 has-text-weight-bold has-text-black")+
            d(h())+
            s()
            , Class="card", id="_modal_go")


if __name__ == '__main__':
    Action([],ANY)
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