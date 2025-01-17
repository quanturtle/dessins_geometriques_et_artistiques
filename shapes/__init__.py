# shapes/__init__.py
from enum import Enum
from shapes.regular_polygons_stars.regular_polygon import draw_regular_polygon
from shapes.regular_polygons_stars.regular_star import draw_regular_star
# from shapes.curves.orbiting_curves import draw_orbiting_curve
# from shapes.curves.rotating_curves import draw_rotating_curve
# from shapes.curves.spiraling_curves import draw_spiraling_curve
# from shapes.designs_from_data.bird_fish import draw_bird_fish
# from shapes.designs_from_data.horse import draw_horse
# from shapes.designs_from_data.lion import draw_lion
# from shapes.designs_from_data.smurf import draw_smurf
# from shapes.elastic_grids.elastic_grid import draw_elastic_grid
# from shapes.folding_paper_dragons.dragon import draw_dragon
# from shapes.fractal_stars.fractal_star import draw_fractal_star
# from shapes.linear_designs.complete_bipartite_graph import draw_complete_bipartite_graph
# from shapes.linear_designs.linear_modules import draw_linear_module
# from shapes.linear_designs.linear_sticks import draw_linear_stick
# from shapes.simple_fractals.simple_fractal import draw_simple_fractal
# from shapes.simple_fractals.simple_fractal_deformed import draw_simple_fractal_deformed
# from shapes.simple_fractals.simple_fractal_rounded import draw_simple_fractal_rounded
# from shapes.surfaces.surface import draw_surface
# from shapes.third_dimension.d3_cube import draw_d3_cube
# from shapes.third_dimension.d3_data import draw_d3_data
# from shapes.third_dimension.d3_structures import draw_d3_structure

class ShapeFunctions(Enum):
    regular_polygon = draw_regular_polygon
    regular_star = draw_regular_star
    # orbiting_curve = draw_orbiting_curve
    # rotating_curve = draw_rotating_curve
    # spiraling_curve = draw_spiraling_curve
    # bird_fish = draw_bird_fish
    # horse = draw_horse
    # lion = draw_lion
    # smurf = draw_smurf
    # elastic_grid = draw_elastic_grid
    # dragon = draw_dragon
    # fractal_star = draw_fractal_star
    # complete_bipartite_graph = draw_complete_bipartite_graph
    # linear_module = draw_linear_module
    # linear_stick = draw_linear_stick
    # simple_fractal = draw_simple_fractal
    # simple_fractal_deformed = draw_simple_fractal_deformed
    # simple_fractal_rounded = draw_simple_fractal_rounded
    # surface = draw_surface
    # d3_cube = draw_d3_cube
    # d3_data = draw_d3_data
    # d3_structure = draw_d3_structure