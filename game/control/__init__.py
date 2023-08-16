"""Module define app wide names.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.08
        revise for wsgi (16).

.. versionadded::    20.07
        add version file.

.. versionadded::    20.07.1
        Support import from other files.

.. versionadded::    22.09
        Support import from other files.

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import os
# name and list your controllers here so their routes become accessible.
# Enable debugging, which gives us tracebacks
project_server = os.path.dirname(os.path.abspath(__file__))
js_dir = os.path.join(project_server, '../view/stlib')
css_dir = os.path.join(project_server, '../../css')
img_dir = os.path.join(project_server, '../../image')
tpl_dir = os.path.join(project_server, '../view/tpl')
inf_dir = os.path.join(project_server, '../..')
py_dir = os.path.join(project_server, '../view')
model_dir = os.path.join(project_server, '../model')
print("js_dir = ", js_dir)
