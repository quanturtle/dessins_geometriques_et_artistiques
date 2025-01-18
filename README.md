# Dessins géométriques et artistiques avec votre micro-ordinateur
> Inspired by https://github.com/v3ga/dessins_geometriques_et_artistiques/  

Recode of book "Dessins géométriques et artistiques avec votre micro-ordinateur" (1985) with python.

## About
In 1985, mathematician Jean-Paul Delahaye used a [Canon X-07](https://en.wikipedia.org/wiki/Canon_X-07) microcomputer with a [X-710 color plotter](https://www.youtube.com/watch?v=JWhNcsYoXQ0) to create incredibly simple yet elegant designs, showcased in his book _Dessins géométriques et artistiques avec votre micro-ordinateur_. Inspired by his work and that of another developer, I decided to port the original BASIC code into Python and use the turtle module to reproduce these captivating designs—just as Delahaye did nearly four decades ago.

![Star](/img/example_star.png)

![Dragon](/img/example_dragon.png)

The precision required to create these designs amazes me, and I wanted to take it a step further by bringing them into the real world in a unique way. My goal was to transform these equations and programs into CAD models, enabling me to 3D print these shapes and capture the same mesmerizing quality in a tangible form.

![8-point star](/img/star8.png)



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

10.  [La troisième dimension](./shapes/third_dimension/)
    * [Le programme D3DATA](./shapes/third_dimension/d3data.py)
    * [Le programme D3CUBE](./shapes/third_dimension/d3cube.py)
    * [Le programme D3STRUCTURES](./shapes/third_dimension/d3structures.py)

## Usage
Demo:
```
python dessins.py demo
```

Generate a shape:
```
python dessins.py <command> <args> --output_stl default=False
```

```
python dessins.py regular_polygon --K 5
python dessins.py dragon --N 8
```

Generate a design:
```
python dessins.py design --N 5
```

Generate a CAD design:
```
python dessins.py design --N 5 --output_stl True
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

Designs: 1-250