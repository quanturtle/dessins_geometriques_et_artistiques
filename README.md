# Dessins géométriques et artistiques avec votre micro-ordinateur
> Inspired by https://github.com/v3ga/dessins_geometriques_et_artistiques/  

Recode of book "Dessins géométriques et artistiques avec votre micro-ordinateur" (1985) with python.

## About
In 1985, mathematician Jean-Paul Delahaye used a [Canon X-07](https://en.wikipedia.org/wiki/Canon_X-07) microcomputer with a [X-710 color plotter](https://www.youtube.com/watch?v=JWhNcsYoXQ0) to create incredibly simple yet elegant designs, showcased in his book _Dessins géométriques et artistiques avec votre micro-ordinateur_. Inspired by his work and that of another developer, I decided to port the original BASIC code into Python and use the turtle module to reproduce these captivating designs—just as Delahaye did four decades ago.

![Star](/img/example_star.png)

![Dragon](/img/example_dragon.png)

The precision required to create these designs amazes me, and I wanted to take it a step further by bringing them into the real world in a unique way. My goal was to transform these equations and programs into CAD models, enabling me to 3D print these shapes and capture the same mesmerizing quality in a tangible form.

| Turtle   | CAD     | Slicer   | Printing |  Printed |
| -------- | ------- | -------- | -------- | -------- |
| ![8-point star Turtle](/img/star8_turtle.png) | ![8-point star CAD](/img/star8_cad.png) | ![8-point star slicer](/img/star8_slicer.png) | ![8-point star printing](/img/star8_printing.png) | ![8-point star printed](/img/star8_printed.png) |

## Index
1. [Polygones, étoiles, etc.](./shapes/polygons_stars/)
   * [Le programme POLYGONES RÉGULIERS](./shapes/polygons_stars/regular_polygon.py)
    * [Le programme ÉTOILES RÉGULIÈRES](./shapes/polygons_stars/regular_star.py)
    * [Le programme COMPOSITION 1](./shapes/polygons_stars/composition_1.py)
    * [Le programme COMPOSITION 2](./shapes/polygons_stars/composition_2.py)
    * [Le programme JOLIGONES](./shapes/polygons_stars/prettygon.py)

2. [Dessins à partir de données](./shapes/designs_from_data/)
    * [Le programme CHEVAL](./shapes/designs_from_data/horse.py)
    * Les programmes [LION](./shapes/designs_from_data/lion.py), [OISEAUX-POISSONS](./shapes/designs_from_data/bird_fish.py), [SMURF](./shapes/designs_from_data/smurf.py)

3. [Dragons de papiers pliés](./shapes/folding_paper_dragons/)
   * [Le programme DRAGONS](./shapes/folding_paper_dragons/dragon.py)

4. [Étoiles fractales](./shapes/fractal_stars/)
   * [Le programme ÉTOILES FRACTALES](./shapes/fractal_stars/fractal_star.py)

5. [Courbes](./shapes/curves/)
    * [Le programme COURBES ORBITALES](./shapes/curves/orbiting_curves.py)
    * [Le programme COURBES TOURNANTES](./shapes/curves/rotating_curves.py)
    * [Le programme COURBES SPIRALES](./shapes/curves/spiraling_curves.py)

6. [Dessins linéaires](./shapes/linear_designs/)
    * [Le programme BIPARTI COMPLET](./shapes/linear_designs/complete_bipartite_graph.py)
    * [Le programme LINÉAIRES MODULO](./shapes/linear_designs/linear_modulo.py)
    * [Le programme LINÉAIRES BÂTONS](./shapes/linear_designs/linear_sticks.py)

7. [Fractales simples](./shapes/simple_fractals/)
    * [Le programme FRACTALES SIMPLES](./shapes/simple_fractals/simple_fractal.py)
    * [Le programme FRACTALES SIMPLES ARRONDIES](./shapes/simple_fractals/simple_fractal_rounded.py)
    * [Le programme FRACTALES SIMPLES DÉFORMÉES](./shapes/simple_fractals/simple_fractal_deformed.py)

8. [Quadrillages élastiques](./shapes/elastic_grids/)
   * [Le programme QUADRILLAGES ÉLASTIQUES](./shapes/elastic_grids/elastic_grid.py)

9. [Surfaces](./shapes/surfaces/)
   * [Le programme SURFACES](./shapes/surfaces/surface.py)

10. [La troisième dimension](./shapes/third_dimension/)
    * [Le programme D3DATA](./shapes/third_dimension/d3data.py)
    * [Le programme D3CUBE](./shapes/third_dimension/d3cube.py)
    * [Le programme D3STRUCTURES](./shapes/third_dimension/d3structures.py)

## Program structure
* `shapes`: contains the original programs
* `designs`: designs using the original programs with modified arguments
* `cad`: pipeline to generate a CAD design that can be 3D printed

## Installation
Install using `uv`:
```sh
uv init
uv sync # or uv pip install -r requirements.txt
```
Test everything is working:
```sh
uv run python dessins.py dragon
```

## Usage
Basic usage:
```sh
python dessins.py <command>
```
where `command` is a shape (like `regular_polygon` or `dragon`).
This will run the standard program from the book.  
The plotting window `NP` is generally set at `480`.

Generate a shape:
```sh
python dessins.py <command> <kwargs> --animate instant --output my_design
```
```sh
--animate: str                      -default: instant, choices=[fast, fastest, instant]
--output:  Optional[str] = None     -default: None (no .stl output)
```
Each shape has `kwargs` that need to be passed or it will default to the original program's arguments.

Examples:
```sh
python dessins.py regular_polygon       # draw standard shape
python dessins.py regular_polygon -K 8  # specify parameter for shape
```
```sh
python dessins.py dragon
python dessins.py dragon -N 8
python dessins.py dragon -N 12
```

Generate a design:
```sh
python dessins.py design_5
```

Generate a CAD design:
```sh
python dessins.py regular_polygon -K 5 --output my_design
```

Shapes:
```
regular_polygon
regular_star
composition_1
composition_2
prettygon

horse
lion
bird_fish
smurf

dragon

fractal_star

orbiting_curves
rotating_curves
spiraling_curves

bipartite_graph

linear_modulo
linear_sticks

simple_fractal
simple_fractal_rounded
simple_fractal_deformed

elastic_grid

surface

d3data
d3cube
d3structures
```