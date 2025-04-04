import sys
import math
import turtle
import argparse
from typing import Callable, List

from cad import generate_cad
from shapes import *
from designs import *


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
        
    elif command in ['design_35', 'design_36', 'design_37', 'design_39', 'design_40', 'design_41']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(-NP, -NP, NP, NP)
    
    # TODO2: fix presentation, design_38, design_41, design_42, design_43
    elif command in ['design_38']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(-0.5*NP, -0.5*NP, 1.5*NP, 1.5*NP)
    
    elif command in ['design_45']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, 1.1*NP, 1.1*NP)
    
    # TODO2: could be better
    elif command in ['design_46', 'design_47']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(-1.3*NP, -1.3*NP, 1.3*NP, 1.3*NP)
        
    elif command in ['design_50', 'design_51', 'design_52']:
        turtle.setup(width=550, height=800)
        turtle.setworldcoordinates(0, 0, 550, 800)
        
    # TODO2: could be better
    elif command in ['design_53', 'design_55', 'design_57', 'design_58', 'design_59', 'design_60', 'design_61']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(-NP, -NP, NP, NP)
        
    elif command in ['design_54', 'design_56']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(-3*NP, -3*NP, 3*NP, 3*NP)
        
    elif command in ['design_80', 'design_82', 'design_83', 'design_84', 'design_92', 'design_93', 'design_94', 'design_96', 'design_99', 'design_100']:
        turtle.setup(width=550, height=800)
        turtle.setworldcoordinates(0, 0, 550, 800)

    elif command in ['design_115', 'design_116', 'design_117']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, 1.2*NP, 1.2*NP)
        
    elif command in ['design_136']:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(-NP, -NP, NP, NP)
    
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


# pts or None if not yet implemented
def draw_shape(draw_function, *args, **kwargs):
    return draw_function(*args, **kwargs)


def post_processing(pts: List = None, name: str = None):
    turtle.hideturtle()
    turtle.update()
    turtle.exitonclick()

    if pts and name:
        generate_cad(pts, name)


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
        "design_50": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_51": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_52": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_53": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_54": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_55": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_56": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_57": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_58": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_59": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_60": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_61": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_62": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_63": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_64": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_177": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_178": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_179": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_180": {
            "help": "Draw a design.",
            "args": {}
        },
        "design_181": {
            "help": "Draw a design.",
            "args": {}
        },
		"design_182": {
            "help": "Draw a design.",
            "args": {}
        },
		"design_183": {
            "help": "Draw a design.",
            "args": {}
        },
  
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
        
        subparser.add_argument("--output",
                               type=str,
                               default=None,
                               required=False,
                               help="Output file name (default: No file output)")
        
    args = parser.parse_args()

    # begin pipeline
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
        "design_50": design_50,
        "design_51": design_51,
        "design_52": design_52,
        "design_53": design_53,
        "design_54": design_54,
        "design_55": design_55,
        "design_56": design_56,
        "design_57": design_57,
        "design_58": design_58,
        "design_59": design_59,
        "design_60": design_60,
        "design_61": design_61,
        "design_62": design_62,
        "design_63": design_63,
        "design_64": design_64,
        "design_177": design_177,
        "design_178": design_178,
        "design_179": design_179,
        "design_180": design_180,
        "design_181": design_181,
        "design_182": design_182,
		"design_183": design_183,
  
    }

    pts = draw_shape(shape_functions[args.command])

    post_processing(pts, name=args.output)
    
    return sys.exit(0)


if __name__ == "__main__":
    main()