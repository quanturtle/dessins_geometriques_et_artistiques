import sys
import math
import turtle
import argparse
from typing import Callable

from shapes import (
    draw_regular_polygon,
    draw_regular_star,
    draw_composition_1,
    draw_composition_2,
    draw_prettygon,
    draw_horse, 
    draw_lion, 
    draw_bird_fish, 
    draw_smurf,
    draw_dragon,
    draw_fractal_star,
    draw_orbiting_curves,
    draw_rotating_curves,
    draw_spiraling_curves,
    draw_complete_bipartite_graph,
    draw_linear_modulo,
    draw_linear_sticks,
    draw_simple_fractal,
    draw_simple_fractal_rounded,
    draw_simple_fractal_deformed,
    draw_elastic_grid,
    draw_surface,
    draw_d3data,
    draw_d3cube,
    draw_d3structures,
)

from designs.polygons_stars import (
    design_1,
    design_2,
    design_3,
    design_4,
    design_5,
    design_6,
    design_7,
    design_8,
    design_9,
    design_10,
    design_11,
    design_12,
    design_13,
    design_14,
    design_15,
    design_16,
    design_17,
    design_18,
    design_19,
    design_20,
    design_21,
    design_22,
    design_23,
    design_24,
    design_25,
    design_26,
    design_27,
    design_28,
    design_29,
    design_30,
    design_31,
    design_32,
    design_33,
)

from designs.designs_from_data import (
    design_34,
    design_35,
    design_36,
    design_37,
    design_38,
    design_39,
    design_40,
    design_41,
    design_42,
    design_43,
)

from designs.folding_paper_dragons import (
    design_50,
    design_51,
    design_52,
    design_53,
    design_54,
    design_55,
    design_56,
    design_57,
    design_58,
    design_59,
    design_60,
    design_61,
    design_62,
    design_63,
    design_64,
)

from designs.fractal_stars import (
    design_65,
    design_66,
    design_67,
    design_68,
    design_69,
    design_70,
    design_71,
    design_72,
    design_73,
    design_74,
    design_75,
    design_76,
    design_77,
)


def setup_canvas(command: str, NP: int, animation: str = "instant"):
    if command == 'dragon':
        turtle.setup(width=550, height=800)
        turtle.setworldcoordinates(0, 0, 550, 800)

    elif command == 'linear_modulo':
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, 1.5*NP, 1.5*NP)
        
    elif command == 'simple_fractal':
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, 1.3*NP, 1.3*NP)
        
    elif command == 'd3data':
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, 1.5*NP, 1.5*NP)

    else:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, NP, NP)
    
    match animation:
        case "instant":
            turtle.tracer(0)
        case "fast":
            turtle.speed("fast")
        case "fastest":
            turtle.speed("fastest")

    turtle.penup()
    turtle.home()


def draw_shape(draw_function, *args, **kwargs):
    draw_function(*args, **kwargs)


def post_processing():
    turtle.hideturtle()
    turtle.update()
    turtle.exitonclick()

    # TODO: add flag for output_stl (True/False) and name if True
    print("Post-processing step (to be defined).")    


def main():
    parser = argparse.ArgumentParser(description="Draw shapes using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    command_parsers = {
        "regular_polygon": {
            "help": "Draw a regular polygon.",
            "args": {
                "-K": {"type": int, "default": 5, "required": False, "help": "Number of sides"},
                "-R": {"type": float, "default": 240*0.45, "required": False, "help": "Radius, NP/2*R"},
                "-AD": {"type": float, "default": math.pi/4, "required": False, "help": "Starting angle in degrees"}
            }
        },
        "regular_star": {
            "help": "Draw a regular star.",
            "args": {
                "-K": {"type": int, "default": 8, "required": False, "help": "Number of points"},
                "-H": {"type": int, "default": 3, "required": False, "help": "Skip H points each time"},
                "-R": {"type": float, "default": 130, "required": False, "help": "Radius"},
                "-AD": {"type": float, "default": math.pi/2, "required": False, "help": "Starting angle in degrees"}
            }
        },
        "composition_1": {
            "help": "Draw a composition of shapes.",
            "args": {
                "-K1": {"type": int, "default": 5, "required": False, "help": "Number of shapes"},
                "-R1": {"type": float, "default": 240*0.27, "required": False, "help": "Radius, NP/2*R1"},
                "-A1": {"type": float, "default": math.pi/2, "required": False, "help": "Starting angle in degrees"},
                "-K": {"type": int, "default": 25, "required": False, "help": "Number of points"},
                "-H": {"type": int, "default": 12, "required": False, "help": "Skip H points each time"},
                "-R": {"type": float, "default": 240*0.22, "required": False, "help": "Radius, NP/2*R"},
                "-AD": {"type": float, "default": math.pi/2, "required": False, "help": "Starting angle in degrees"}
            }
        },
        "composition_2": {
            "help": "Draw a composition of shapes.",
            "args": {
                "-K1": {"type": int, "default": 5, "required": False, "help": "Number of shapes"},
                "-N": {"type": int, "default": 32, "required": False, "help": "Number of shapes"},
                "-K": {"type": int, "default": 16, "required": False, "help": "Number of points"},
                "-H": {"type": int, "default": 5, "required": False, "help": "Skip H points each time"},
                "-R1": {"type": float, "default": 240*0.36, "required": False, "help": "Radiusm, NP/2*R1"},
                "-R": {"type": float, "default": 240*0.14, "required": False, "help": "Radius, NP/2*R"},
                "-RR": {"type": float, "default": 0.9, "required": False, "help": "Radius ratio"},
            }
        },
        "prettygon": {
            "help": "Draw a prettygon.",
            "args": {
                "-K": {"type": int, "default": 5, "required": False, "help": "Number of sides"},
                "-AN": {"type": float, "default": 15*(math.pi/31), "required": False, "help": "Angle"},
                "-RA": {"type": float, "default": 0.98, "required": False, "help": "Radius ratio"},
                "-AA": {"type": float, "default": 0.0, "required": False, "help": "Starting angle"},
                "-RR": {"type": float, "default": 480*0.80, "required": False, "help": "Radius, NP*R"},
                "-initial_y": {"type": float, "default": 0, "required": False, "help": "Initial y-coordinate"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
                
            }
        },
        "horse": {"help": "Draw a horse.", "args": {}},
        "lion": {"help": "Draw a lion.", "args": {}},
        "bird_fish": {"help": "Draw a bird or a fish.", "args": {}},
        "smurf": {"help": "Draw a smurf.", "args": {}},
        "dragon": {
            "help": "Draw a dragon.", "args": {
                "-N": {"type": int, "default": 10, "required": False, "help": "Number of iterations"},
            }
        },
        "fractal_star": {
            "help": "Draw a fractal star.",
            "args": {
                "-N": {"type": int, "default": 5, "required": False, "help": "Number of points"},
                "-K": {"type": int, "default": 5, "required": False, "help": "Number of iterations"},
                "-RA": {"type": float, "default": 0.35, "required": False, "help": "Radius ratio"},
                "-LL": {"type": float, "default": 480*0.6, "required": False, "help": "Line length"},
                "-AA": {"type": float, "default": 4*math.pi/5, "required": False, "help": "Angle"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "orbiting_curves": {
            "help": "Draw orbiting curves.",
            "args": {
                "-N": {"type": int, "default": 2000, "required": False, "help": "Number of iterations"},
                "-T1": {"type": int, "default": 2, "required": False, "help": "Time factor 1"},
                "-T2": {"type": int, "default": 100, "required": False, "help": "Time factor 2"},
                "-K1": {"type": int, "default": 1, "required": False, "help": "Number of points 1"},
                "-K2": {"type": int, "default": 1, "required": False, "help": "Number of points 2"},
                "-R1": {"type": float, "default": 480*0.25, "required": False, "help": "Radius 1"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "rotating_curves": {
            "help": "Draw rotating curves.",
            "args": {
                "-N": {"type": int, "default": 2000, "required": False, "help": "Number of iterations"},
                "-T1": {"type": int, "default": 1, "required": False, "help": "Time factor 1"},
                "-T2": {"type": int, "default": 100, "required": False, "help": "Time factor 2"},
                "-K1": {"type": int, "default": 1, "required": False, "help": "Number of points 1"},
                "-K2": {"type": int, "default": 1, "required": False, "help": "Number of points 2"},
                "-H1": {"type": int, "default": 1, "required": False, "help": "Skip points 1"},
                "-H2": {"type": int, "default": 1, "required": False, "help": "Skip points 2"},
                "-R1": {"type": float, "default": 480*0.6, "required": False, "help": "Radius 1"},
                "-R2": {"type": float, "default": 480*0.4, "required": False, "help": "Radius 2"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "spiraling_curves": {
            "help": "Draw spiraling curves.",
            "args": {
                "-N": {"type": int, "default": 2000, "required": False, "help": "Number of iterations"},
                "-T": {"type": int, "default": 40, "required": False, "help": "Time factor"},
                "-R": {"type": float, "default": 0.8, "required": False, "help": "Radius"},
                "-L": {"type": float, "default": 0.1, "required": False, "help": "Length"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "complete_bipartite_graph": {
            "help": "Draw a complete bipartite graph.",
            "args": {
                "-N": {"type": int, "default": 10, "required": False, "help": "Number of vertices in the first set"},
                "-XA": {"type": int, "default": 0, "required": False, "help": "XA"},
                "-YA": {"type": int, "default": 0, "required": False, "help": "YA"},
                "-XB": {"type": int, "default": 0, "required": False, "help": "XB"},
                "-YB": {"type": int, "default": 480, "required": False, "help": "YB"},
                "-XC": {"type": int, "default": 480, "required": False, "help": "XC"},
                "-YC": {"type": int, "default": 0, "required": False, "help": "YC"},
                "-XD": {"type": int, "default": 480, "required": False, "help": "XD"},
                "-YD": {"type": int, "default": 480, "required": False, "help": "YD"},
            }
        },
        "linear_modulo": {
            "help": "Draw linear modulo.",
            "args": {
                "-N": {"type": int, "default": 10, "required": False, "help": "Number of points"},
                "-M": {"type": int, "default": 10, "required": False, "help": "Number of curves"},
                "-K1": {"type": float, "default": 4, "required": False, "help": "K1"},
                "-K2": {"type": float, "default": 5, "required": False, "help": "K2"},
                "-H": {"type": int, "default": 2, "required": False, "help": "H"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "linear_sticks": {
            "help": "Draw linear sticks.",
            "args": {
                "-N": {"type": int, "default": 10, "required": False, "help": "Number of points"},
                "-M": {"type": int, "default": 1, "required": False, "help": "Number of sticks"},
                "-K": {"type": int, "default": 5, "required": False, "help": "Modulo"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "simple_fractal": {
            "help": "Draw a simple fractal.",
            "args": {
                "-M": {"type": int, "default": 3, "required": False, "help": "M"},
                "-N": {"type": int, "default": 4, "required": False, "help": "N"},
                "-K": {"type": int, "default": 4, "required": False, "help": "K"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "simple_fractal_rounded": {
            "help": "Draw a simple fractal with rounded corners.",
            "args": {
                "-M": {"type": int, "default": 3, "required": False, "help": "M"},
                "-N": {"type": int, "default": 4, "required": False, "help": "N"},
                "-K": {"type": int, "default": 4, "required": False, "help": "K"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "simple_fractal_deformed": {
            "help": "Draw a simple fractal with deformed corners.",
            "args": {
                "-M": {"type": int, "default": 3, "required": False, "help": "M"},
                "-N": {"type": int, "default": 4, "required": False, "help": "N"},
                "-K": {"type": int, "default": 4, "required": False, "help": "K"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "elastic_grid": {
            "help": "Draw an elastic grid.",
            "args": {
                "-deformation_subroutine": {"type": Callable, "default": lambda di: di**0.3 if di < 1 else di, "required": False, "help": "Deformation subroutine"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "surface": {
            "help": "Draw a surface.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "d3data": {
            "help": "Draw a 3D data.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "d3cube": {
            "help": "Draw a 3D cube.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "d3structures": {
            "help": "Draw 3D structures.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Window size"},
            }
        },
        "design": {
            "help": "Draw a design.",
            "args": {}
        }
    }

    for cmd_name, cmd_config in command_parsers.items():
        subparser = subparsers.add_parser(cmd_name, help=cmd_config["help"])
        
        for arg_name, arg_config in cmd_config["args"].items():
            subparser.add_argument(arg_name, **arg_config)
        
        subparser.add_argument("--animation", 
                             choices=["fast", "fastest", "instant"],
                             default="instant",
                             required=False,
                             help="Animation speed (default: instant)")
        
    args = parser.parse_args()

    NP = 480
    
    setup_canvas(args.command, NP, args.animation)

    shape_functions = {
        "regular_polygon": draw_regular_polygon,
        "regular_star": draw_regular_star,
        "composition_1": draw_composition_1,
        "composition_2": draw_composition_2,
        "prettygon": draw_prettygon,
        "horse": draw_horse,
        "lion": draw_lion,
        "bird_fish": draw_bird_fish,
        "smurf": draw_smurf,
        "dragon": draw_dragon,
        "fractal_star": draw_fractal_star,
        "orbiting_curves": draw_orbiting_curves,
        "rotating_curves": draw_rotating_curves,
        "spiraling_curves": draw_spiraling_curves,
        "complete_bipartite_graph": draw_complete_bipartite_graph,
        "linear_modulo": draw_linear_modulo,
        "linear_sticks": draw_linear_sticks,
        "simple_fractal": draw_simple_fractal,
        "simple_fractal_rounded": draw_simple_fractal_rounded,
        "simple_fractal_deformed": draw_simple_fractal_deformed,
        "elastic_grid": draw_elastic_grid,
        "surface": draw_surface,
        "d3data": draw_d3data,
        "d3cube": draw_d3cube,
        "d3structures": draw_d3structures,
        "design": design_67
    }

    draw_shape(shape_functions[args.command])

    # Post-processing step
    post_processing()
    
    return sys.exit(0)


if __name__ == "__main__":
    main()