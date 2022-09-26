#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SupyPlay
# Copyright 2010–2022 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.activufrj.nce.ufrj.br>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# SupyPlay é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>
"""Conecta com a fonte dos dados, neste caso a API do Github..

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------

.. versionadded::    22.09
        Fix for new version of Pygithub.

"""

"""
############################################################
SuPyGirls - Data Source
############################################################

Conecta com a fonte dos dados, neste caso a API do Github.

"""
import datetime
import os.path
import os as op
from github import Github
from base64 import decodebytes as dcd

TIMESTAMP = '@{:%Y-%m-%d %H:%M}'

LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/git/spg'))
REMOTE_URL = "https://github.com/SuPyPackage/SuPyGirls.git"
USERNAME = "kwarwp"
PASSWORD = dcd(str.encode(op.environ["IKW"])).decode("utf-8")
TOKEN = dcd(str.encode(op.environ["IKT"])).decode("utf-8")
print("TOKEN", TOKEN)
# str(dcd(str.encode(op.environ["IKW"])))
# USERNAME = "carlotolla"
# PASSWORD = op.environ["ISME"]


def spike():

    g = Github(TOKEN)
    u = g.get_user()
    r = None
    for repo in u.get_repos():
        if "SuPyGirls" in str(repo.name):
            r = repo
            break
        print(type(repo.name), repo.name)

    rp = u.get_repo("supyjogo")  # "activlets")

    print(r)
    [print(org) for org in rp.get_branches()]
    al = rp.get_branch("uva")
    cm = al.commit

    print(al.etag, al.commit.sha)
    print("cont", rp.get_contents("/uva/main.py", cm.sha).decoded_content)


class DataSource:
    def __init__(self):
        # g = Github(USERNAME, PASSWORD)
        g = Github(TOKEN)
        g.get_user("kwarwp")
        self.user = g.get_user("kwarwp")
        # print("DataSource", g, self.user)
        self.repo = None

    def get_file_branched(self, project, packager, moduler="main.py"):
        self.repo = self.user.get_repo(project)
        self.repo.get_branches()
        ref = self.repo.get_branch(packager).commit.sha
        return self.repo.get_contents("{}/{}".format(packager, moduler), ref)

    def get_file_contents(self, project, packager, moduler="main.py"):
        self.repo = self.user.get_repo(project)
        path = "{}/{}" if packager else "{}{}"
        print("get_file_contents ", project, path.format(packager, moduler))
        return self.repo.get_contents(path.format(packager, moduler))

    def create_file(self, project, filename, decoded_content, comment=None):
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = comment if comment else "Created {} {}".format(filename, timestamp)
        self.repo = self.user.get_repo(project)
        self.repo.create_file("/{}".format(filename), comment, decoded_content)
        return comment
    """
    def create_project(self, project):
        curl -i -H 'Authorization: token TOKEN' -d '{"name":"grete"}' https://api.github.com/user/repos
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = "Created {} at {}".format(project, timestamp)
        self.user.create_repo("/{}".format(project), comment)
        return comment
    """

    def save_file(self, project, filename, decoded_content, comment=None):
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = comment if comment else "Saved {} {}".format(filename, timestamp)
        self.repo = self.user.get_repo(project)
        file = self.repo.get_contents(filename)
        self.repo.update_file("/{}".format(filename), comment, decoded_content, file.sha)
        return comment

    def append_file(self, project, filename, decoded_content, comment=None):
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = comment if comment else "Saved {} {}".format(filename, timestamp)
        self.repo = self.user.get_repo(project)
        file = self.repo.get_contents(filename)
        file_content = dcd(str.encode(file.content)).decode("utf-8") + decoded_content
        self.repo.update_file("/{}".format(filename), comment, file_content, file.sha)
        return comment

    def update_file(self, project, packager, decoded_content, moduler="main.py", comment=None):
        timestamp = TIMESTAMP.format(datetime.datetime.now())
        comment = comment if comment else "Automatic save {}".format(timestamp)
        file = self.get_file_contents(project, packager)
        self.repo.update_file("{}/{}".format(packager, moduler), comment, decoded_content, file.sha)
        return comment

    def get_branches(self, project):
        self.repo = self.user.get_repo(project)
        return self.repo.get_branches()


DS = DataSource()
