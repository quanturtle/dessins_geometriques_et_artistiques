from cad import capture_points

from .curves import (
    draw_orbiting_curves,
    draw_rotating_curves,
    draw_spiraling_curves
)


from .designs_from_data import (
    draw_horse,
    draw_lion,
    draw_bird_fish,
    draw_smurf
)


from .elastic_grids import (
    draw_elastic_grid
)


from .folding_paper_dragons import (
    draw_dragon
)


from .fractal_stars import (
    draw_fractal_star
)


from .linear_designs import (
    draw_complete_bipartite_graph,
    draw_linear_modulo,
    draw_linear_sticks
)


from .polygons_stars import (
    draw_regular_polygon,
    draw_regular_star,
    draw_composition_1,
    draw_composition_2,
    draw_prettygon,
)


from .simple_fractals import (
    draw_simple_fractal,
    draw_simple_fractal_deformed,
    draw_simple_fractal_rounded
)


from .surfaces.surface import (
    draw_surface
)


from .third_dimension import (
    draw_d3cube,
    draw_d3data,
    draw_d3structures
)


for _name, _func in list(globals().items()):
    if _name.startswith("draw_"):
        globals()[_name] = capture_points(_func)


__all__ = [
    "draw_orbiting_curves",
    "draw_rotating_curves",
    "draw_spiraling_curves",
    "draw_horse",
    "draw_lion",
    "draw_bird_fish",
    "draw_smurf",
    "draw_elastic_grid",
    "draw_dragon",
    "draw_fractal_star",
    "draw_complete_bipartite_graph",
    "draw_linear_modulo",
    "draw_linear_sticks",
    "draw_regular_polygon",
    "draw_regular_star",
    "draw_composition_1",
    "draw_composition_2",
    "draw_prettygon",
    "draw_simple_fractal",
    "draw_simple_fractal_deformed",
    "draw_simple_fractal_rounded",
    "draw_surface",
    "draw_d3cube",
    "draw_d3data",
    "draw_d3structures",
]