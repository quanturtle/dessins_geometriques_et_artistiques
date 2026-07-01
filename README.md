# Dessins géométriques et artistiques avec votre micro-ordinateur
> Inspired by https://github.com/v3ga/dessins_geometriques_et_artistiques/  

Recode of book "Dessins géométriques et artistiques avec votre micro-ordinateur" (1985) with python.

[Dessins géométriques et artistiques avec votre micro-ordinateur](https://nextcloud.univ-lille.fr/index.php/s/R4PgSRWGyHEbDgG)
[Nouveaux dessins géométriques et artistiques avec votre micro-ordinateur](https://nextcloud.univ-lille.fr/index.php/s/cwXAAokbbeaykW6)

## About
In 1985, mathematician Jean-Paul Delahaye used a [Canon X-07](https://en.wikipedia.org/wiki/Canon_X-07) microcomputer with a [X-710 color plotter](https://www.youtube.com/watch?v=JWhNcsYoXQ0) to create incredibly simple yet elegant designs, showcased in his book _Dessins géométriques et artistiques avec votre micro-ordinateur_. Inspired by his work and that of another developer, I decided to port the original BASIC code into Python and use the turtle module to reproduce these captivating designs—just as Delahaye did four decades ago.

![Star](/img/example_star.png)

![Dragon](/img/example_dragon.png)

The precision required to create these designs amazes me, and I wanted to take it a step further by bringing them into the real world in a unique way. My goal was to transform these equations and programs into CAD models, enabling me to 3D print these shapes and capture the same mesmerizing quality in a tangible form.

| Turtle   | CAD     | Slicer   | Printing |  Printed |
| -------- | ------- | -------- | -------- | -------- |
| ![8-point star Turtle](/img/star8_turtle.png) | ![8-point star CAD](/img/star8_cad.png) | ![8-point star slicer](/img/star8_slicer.png) | ![8-point star printing](/img/star8_printing.png) | ![8-point star printed](/img/star8_printed.png) |

## Index
1. Polygones, étoiles, etc. (designs 1-33, [designs/polygons_stars.py](./designs/polygons_stars.py))
    * [Le programme POLYGONES RÉGULIERS](./shapes/regular_polygon.py)
    * [Le programme ÉTOILES RÉGULIÈRES](./shapes/regular_star.py)
    * [Le programme COMPOSITION 1](./shapes/composition_1.py)
    * [Le programme COMPOSITION 2](./shapes/composition_2.py)
    * [Le programme JOLIGONES](./shapes/prettygon.py)

2. Dessins à partir de données (designs 34-49, [designs/designs_from_data.py](./designs/designs_from_data.py))
    * [Le programme CHEVAL](./shapes/horse.py)
    * Les programmes [LION](./shapes/lion.py), [OISEAUX-POISSONS](./shapes/bird_fish.py), [SMURF](./shapes/smurf.py)

3. Dragons de papiers pliés (designs 50-64, [designs/folding_paper_dragons.py](./designs/folding_paper_dragons.py))
    * [Le programme DRAGONS](./shapes/dragon.py)

4. Étoiles fractales (designs 65-77, [designs/fractal_stars.py](./designs/fractal_stars.py))
    * [Le programme ÉTOILES FRACTALES](./shapes/fractal_star.py)

5. Courbes (designs 78-100, [designs/curves.py](./designs/curves.py))
    * [Le programme COURBES ORBITALES](./shapes/orbiting_curves.py)
    * [Le programme COURBES TOURNANTES](./shapes/rotating_curves.py)
    * [Le programme COURBES SPIRALES](./shapes/spiraling_curves.py)

6. Dessins linéaires (designs 101-114, [designs/linear_designs.py](./designs/linear_designs.py))
    * [Le programme BIPARTI COMPLET](./shapes/complete_bipartite_graph.py)
    * [Le programme LINÉAIRES MODULO](./shapes/linear_modulo.py)
    * [Le programme LINÉAIRES BÂTONS](./shapes/linear_sticks.py)

7. Fractales simples (designs 115-163, [designs/simple_fractals.py](./designs/simple_fractals.py))
    * [Le programme FRACTALES SIMPLES](./shapes/simple_fractal.py)
    * [Le programme FRACTALES SIMPLES ARRONDIES](./shapes/simple_fractal_rounded.py)
    * [Le programme FRACTALES SIMPLES DÉFORMÉES](./shapes/simple_fractal_deformed.py)

8. Quadrillages élastiques (designs 164-176, [designs/elastic_grids.py](./designs/elastic_grids.py))
    * [Le programme QUADRILLAGES ÉLASTIQUES](./shapes/elastic_grid.py)

9. Surfaces (designs 177-200, [designs/surfaces.py](./designs/surfaces.py))
    * [Le programme SURFACES](./shapes/surface.py)

10. La troisième dimension (designs 201-252, [designs/third_dimension.py](./designs/third_dimension.py))
    * [Le programme D3DATA](./shapes/d3data.py)
    * [Le programme D3CUBE](./shapes/d3cube.py)
    * [Le programme D3STRUCTURES](./shapes/d3structures.py)

## Program structure
* `shapes/`: the original programs, one module per program; `shapes.SHAPES` maps each shape name to its draw function
* `designs/`: the catalog of numbered designs, one module per book chapter; each entry in `designs.DESIGNS` records the draw function, its parameters, and its canvas window
* `cad/`: pipeline to generate a CAD design that can be 3D printed (STL files land in `output/`)
* `dessins.py`: the command-line interface

## Installation
Install using `uv`:
```sh
uv sync
```
Test everything is working:
```sh
uv run python dessins.py shape dragon
```

## Usage
Basic usage:
```sh
python dessins.py <command> <shape_name|design_number>
```
where `command` is `shape|design`. After that, the user provides a `shape_name` (if `shape` was selected). If `design` was provided by the user, the `design_number` needs to be selected.
This will run the standard program from the book.
The plotting window `NP` is generally set at `480`.

Generate a shape:
```sh
python dessins.py shape <shape_name> <kwargs> --animation instant --output my_design
```
```sh
--animation: str                    -default: instant, choices=[fast, fastest, instant]
--output:    Optional[str] = None   -default: None (no .stl output; files land in output/)
```
Each shape exposes its numeric parameters as flags (see `python dessins.py shape <shape_name> --help`); anything not passed defaults to the original program's arguments.

Examples:
```sh
python dessins.py shape regular_polygon       # draw standard shape
python dessins.py shape regular_polygon -K 8  # specify parameter for shape
```
```sh
python dessins.py shape dragon
python dessins.py shape dragon -N 8
python dessins.py shape dragon -N 12
```

Generate a design:
```sh
python dessins.py design 5
```

Generate a CAD design:
```sh
python dessins.py shape regular_polygon -K 5 --output my_design
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

complete_bipartite_graph

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