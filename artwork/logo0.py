#! /usr/bin/env python
# -*- coding: UTF8 -*-
""" Modelo em pov-ray do logo LABASE

Changelog
---------
.. versionadded::    23.07
   |br| versão inicial (27)

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

"""
__version__ = "23.07"

from vapory import *


class Ball:
    def __init__(self):
        mycamera = Camera('location', [0, 2, -3], 'look_at', [0, 1, 2])
        light = LightSource([2, 4, -3], 'color', [1, 1, 1])
        sphere = Sphere([0, 1, 2], 2, Texture(Pigment('color', [1, 0, 1])))
        scene = Scene(camera=mycamera,  # a Camera object
                      objects=[light, sphere],  # POV-Ray objects (items, lights)
                      # atmospheric=[fog],  # Light-interacting objects
                      included=["colors.inc"])  # headers that POV-Ray may need

        scene.render("logo0.png",  # output to a PNG image file
                     width=600, height=400,  # in pixels. Determines the camera ratio.
                     antialiasing=0.01,  # The nearer from zero, the more precise the image.
                     quality=1)  # quality=1 => no shadow/reflection, quality=10 is 'normal'


class Pawn:
    def __init__(self):
        objects = [

            # SUN
            LightSource([1500, 2500, -2500], 'color', 1),
            # PAWN
            Sphere([0, 0.4, 0], 0.05, 'scale', [0.2, 1.75, 1.75], 'rotate', [0, 75, 0],
                   # Cone([0, 0, 0], 0.5, [0, 1, 0], 0.0),
                   # Texture(Pigment('color', [1, 0.65, 0])),
                   Texture(Pigment('color', [1.1 * e for e in [0.80, 0.48, 0.35]]),
                           # Normal('bumps', 0.15, 'scale', 0.005),
                           # Finish('phong', 0.1)
                           )
                   ),
            Sphere([0.1, 0.4, 0], 0.25, 'scale', [0.5, 1.75, 1.75], 'rotate', [0, 75, 0],
                   # Texture(Pigment('color', [1.1 * e for e in [0.55, 0.38, 0.15]]),
                   Texture(Pigment('color', [0.55, 0.38, 0.15]),
                           # Finish('metallic', 0.9),
                           # Finish('metallic', 0.2, 'specular', 0.75, 'reflection', 0.75))),
                           Finish('metallic', 0.6, 'specular', 0.75))),
            Object(Difference(Sphere([0.0, 0.4, -0.1], 0.35, 'scale', [0.2, 1.75, 1.75], 'rotate', [0, 125, 0],
                                     Texture(Pigment('color', [0.13, 0.11, 0.1]),
                                             Finish('phong', 1))),
                              Sphere([0.0, 0.3, 0.0], 0.35, 'scale', [1.75, 1.75, 1.75], 'rotate', [0, 125, 0],
                                     Texture(Pigment('color', [0.1, 0.15, 0.1]),
                                             Finish('phong', 1)))))

        ]
        scene = Scene(Camera('ultra_wide_angle',
                             'angle', 45,
                             'location', [0.0, 0.6, -3.0],
                             'look_at', [0.0, 0.6, 0.0]
                             ),

                      objects=objects,
                      included=['colors.inc']
                      )

        scene.render('logo0.png', remove_temp=True)


class Lens:
    def __init__(self):
        sun = LightSource([1000, 2500, -2500], 'color', 'White')

        sky = SkySphere(Pigment('gradient', [0, 1, 0],
                                ColorMap([0.0, 'color', 'White'],
                                         [0.5, 'color', 'CadetBlue'],
                                         [1.0, 'color', 'CadetBlue']),
                                "quick_color", "White"))

        ground = Plane([0, 1, 0], 0,
                       Texture(Pigment('color', [0.85, 0.55, 0.30]),
                               Finish('phong', 0.1)
                               )
                       )

        balls = Object(Union(*[Sphere([0, 0, i], 0.35,
                                      Texture(Pigment('color', [1, 0.65, 0]),
                                              Finish('phong', 1)))
                               for i in range(20)]),

                       'scale', [0.4, 0.75, 0.75],
                       'rotate', [0, 5, 0],
                       'translate', [-1.9, 0.5, 0])

        box = Box([-1, -1, -1], [1, 1, 1],
                  'scale', [1.5, 0.75, 0.75],
                  'rotate', [0, 35, 0],
                  'translate', [1.75, 1.2, 4.0],
                  Texture(Pigment('Candy_Cane',
                                  'scale', 0.5,
                                  'translate', [-2.0, 0, 0],
                                  'quick_color', 'Orange'),
                          Finish('phong', 1)
                          )
                  )

        r, over = 6.0, 0.1  # sphere radius, and spheres overlap

        lens = Intersection(Sphere([0, 0, 0], r, 'translate', [0, 0, -r + over]),
                            Sphere([0, 0, 0], r, 'translate', [0, 0, r - over]),
                            Texture('T_Glass3'),
                            Interior('I_Glass3'),
                            'translate', [0, 1.2, 0])

        scene = Scene(Camera('angle', 75,
                             'location', [0.0, 1.0, -3.0],
                             'look_at', [-0.3, 1.0, 0.0]),
                      objects=[sun, sky, ground, balls, box, lens],
                      included=["colors.inc", "textures.inc", "glass.inc"],
                      defaults=[Finish('ambient', 0.1, 'diffuse', 0.9)])

        scene.render("lens.png", width=400, height=300, antialiasing=0.01)


if __name__ == '__main__':
    # Lens()
    Pawn()
    # Ball()

# passing 'ipython' as argument at the end of an IPython Notebook cell
# will display the picture in the IPython notebook.
# scene.render('python3', width=1000, height=500)

# passing no 'file' arguments returns the rendered image as a RGB numpy array
# image = scene.render(width=300, height=500)
