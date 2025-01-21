import sys
import math
import turtle
import argparse

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
    draw_fractal_star
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


def setup_canvas(command: str, NP: int, animation: str = "instant"):
    if command == 'dragon':
        turtle.setup(width=550, height=800)
        turtle.setworldcoordinates(0, 0, 550, 800)

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
    turtle.pendown()


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
                "-R": {"type": float, "default": 240*0.45, "required": False, "help": "Radius"},
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
            "args": {}
        },
        "composition_2": {
            "help": "Draw a composition of shapes.",
            "args": {}
        },
        "prettygon": {
            "help": "Draw a prettygon.",
            "args": {
                "-K": {"type": int, "default": 5, "required": False, "help": "Number of sides"},
                "-R": {"type": int, "default": 100, "required": False, "help": "Radius"}
            }
        },
        "horse": {"help": "Draw a horse.", "args": {}},
        "lion": {"help": "Draw a lion.", "args": {}},
        "bird_fish": {"help": "Draw a bird or a fish.", "args": {}},
        "smurf": {"help": "Draw a smurf.", "args": {}},
        "dragon": {"help": "Draw a dragon.", "args": {}},
        "fractal_star": {
            "help": "Draw a fractal star.",
            "args": {
                "-D": {"type": int, "default": 3, "required": False, "help": "Depth of recursion"}
            }
        },
        "design": {"help": "Draw a design.", "args": {}}
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
        "design": design_50
    }

    draw_shape(shape_functions[args.command])

    # Post-processing step
    post_processing()
    
    return sys.exit(0)


if __name__ == "__main__":
    main()