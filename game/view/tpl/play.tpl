<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{pagetitle}}</title>
    <meta http-equiv="content-type" content="application/xml;charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8">
    <link rel="shortcut icon" href="/image/favicon.ico" type="image/x-icon"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- stylesheets
    % for css in brython_css:
    <link rel="stylesheet" href="/css/{{ css }}.css" type="text/css"/>
    % end
    % for scp in brython_js:
    <script type="text/javascript" src="/js/{{ scp  }}.js"></script>
    % end
    scripts -->
    <script type="text/javascript" src="http://www.glowscript.org/lib/jquery/1.1/jquery.min.js"></script>
    <script type="text/javascript" src="http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/brython@3.8.10/brython.js">
    </script>
    <script src="https://cdn.jsdelivr.net/npm/brython@3.8.10/brython_stdlib.js">
    </script>
<style>
    @keyframes fade {
        from {
            opacity: 1.0;
        }
        to {
            opacity: 0.0;
        }
    }

    .arena {
        transform: translate(-50%, -50%);
    }
</style>

<script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function () {

        // Get all "navbar-burger" elements
        var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

        // Check if there are any navbar burgers
        if ($navbarBurgers.length > 0) {

            // Add a click event on each of them
            $navbarBurgers.forEach(function ($el) {
                $el.addEventListener('click', function () {

                    // Get the target from the "data-target" attribute
                    var target = $el.dataset.target;
                    var $target = document.getElementById(target);

                    // Toggle the class on both the "navbar-burger" and the "navbar-menu"
                    $el.classList.toggle('is-active');
                    $target.classList.toggle('is-active');

                });
            });
        }

    });

</script>
<script type="text/javascript">
    function decodeUnicode(str) {
        // Going backwards: from bytestream, to percent-encoding, to original string.
        return decodeURIComponent(atob(str).split('').map(function (c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
    }
</script>

<script type="text/python">
            from browser import document. window, html, alert
            from browser import ajax, timer
            from browser.local_storage import storage
            from _core.main import Main
            class MockBrython:
                document = document
                window = window
                html = html
                alert = alert
                ajax = ajax
                timer = timer
                storage = storage
                codename = "{{ pagetitle.replace(" - ", ".").lower() }}"
                code = """{{code}}"""
            main = Main(br=MockBrython)
            main.{{"play()"}}


</script>

<!--
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

"""Brython front end client.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""

-->
</head>
<body onLoad="brython({debug:1, cache:'browser', static_stdlib_import:true,
 pythonpath :['__code','__code/{{mod}}']})">
<!-- navigation -->
<!-- % '' if pagetitle.startswith("PLAY - ") else include('menu.tpl') -->
<!-- end navigation -->
<!-- identification -->
<!-- end identification -->
<!-- page content -->
<div class="main-content">
    <div class="container">
        <!-- start of about -->
        <div class="columns is-multiline is-centered">
            <!-- start of about -->
            <div class="column is-12">
                <div id="pyparent" class="card">
                    <!-- about content -->
                    <div id="pycard"></div>
                    <div id="pydiv" class="card is-12by8" style="min-height:600px;">
                        <figure>
                            <img src="/image/{{image}}" width="1000px" alt="Image">
                        </figure>
                    </div>
                </div>
            </div>
            <!-- end of about column -->
        </div>
        <!-- end of about columns -->
    </div>
</div>
<!-- end of page content -->
</body>
</html>
