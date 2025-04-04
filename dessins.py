import sys
import math
import turtle
import argparse
from typing import List, Dict, Optional

from cad import generate_cad
from shapes import *
from designs import *


def setup_canvas(command: str, NP: int, animation: str = "instant"):
    if command.startswith('design_'):
        design_num = int(command.split('_')[1])
        
        if design_num in [35, 36, 37, 39, 40, 41, 136]:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(-NP, -NP, NP, NP)
        
        elif design_num in [46, 47]:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(-1.3*NP, -1.3*NP, 1.3*NP, 1.3*NP)
        
        elif design_num in [54, 56]:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(-3*NP, -3*NP, 3*NP, 3*NP)
        
        elif design_num == 38:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(-0.5*NP, -0.5*NP, 1.5*NP, 1.5*NP)
        
        elif design_num in [50, 51, 52, 80, 82, 83, 84, 92, 93, 94, 96, 99, 100]:
            turtle.setup(width=550, height=800)
            turtle.setworldcoordinates(0, 0, 550, 800)
        
        elif design_num in [45, 115, 116, 117]:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(0, 0, 1.1*NP, 1.2*NP)
        
        elif design_num in [53, 55, 57, 58, 59, 60, 61]:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(-NP, -NP, NP, NP)
        
        else:
            turtle.setup(width=NP, height=NP)
            turtle.setworldcoordinates(0, 0, NP, NP)
    
    else:
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
    return draw_function(*args, **kwargs)


def post_processing(pts: Optional[List] = None, name: Optional[str] = None):
    turtle.hideturtle()
    turtle.update()
    
    if pts and name:
        generate_cad(pts, name)
    
    turtle.exitonclick()


def get_shape_args() -> Dict[str, Dict]:
    return {
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

    }


def get_available_shapes() -> List[str]:
    shapes = []
    
    for name in dir(sys.modules['shapes']):
        if name.startswith('draw_'):
            shapes.append(name[5:])  # Remove 'draw_' prefix
    
    return shapes


def get_available_designs() -> List[str]:
    designs = []
    
    for name in dir(sys.modules['designs']):
        if name.startswith('design_'):
            design_number = name.split('_')[1]
            designs.append(design_number)
    
    return designs


def initialize_parsers():
    parser = argparse.ArgumentParser(description="Draw shapes and designs using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    common_args = {
        "--animation": {
            "choices": ["fast", "fastest", "instant"],
            "default": "instant",
            "required": False,
            "help": "Animation speed (default: instant)"
        },
        "--output": {
            "type": str,
            "default": None,
            "required": False,
            "help": "Output file name (default: No file output)"
        }
    }
    
    shape_parser = subparsers.add_parser("shape", help="Draw predefined shapes")
    shape_subparsers = shape_parser.add_subparsers(dest="shape_name", required=True)
    
    shape_args = get_shape_args()
    available_shapes = get_available_shapes()
    
    for shape_name in available_shapes:
        if shape_name in shape_args:
            shape_config = shape_args[shape_name]
            subparser = shape_subparsers.add_parser(shape_name, help=shape_config["help"])
            
            for arg_name, arg_config in shape_config["args"].items():
                subparser.add_argument(arg_name, **arg_config)
            
            for arg_name, arg_config in common_args.items():
                subparser.add_argument(arg_name, **arg_config)
        else:
            subparser = shape_subparsers.add_parser(shape_name, help=f"Draw a {shape_name}")
    
            for arg_name, arg_config in common_args.items():
                subparser.add_argument(arg_name, **arg_config)
    
    design_parser = subparsers.add_parser("design", help="Draw predefined designs")
    
    design_parser.add_argument("design_number", help="Design number to draw")
    
    for arg_name, arg_config in common_args.items():
        design_parser.add_argument(arg_name, **arg_config)
    
    return parser


def main():
    parser = initialize_parsers()
    args = parser.parse_args()
    
    NP = 480
    
    if args.command == "shape":
        shape_name = args.shape_name
        draw_function_name = f"draw_{shape_name}"
        
        try:
            draw_function = getattr(sys.modules['shapes'], draw_function_name)
            command = shape_name

        except AttributeError:
            print(f"Error: Shape '{shape_name}' not found in shapes module.")
            return sys.exit(1)
        
        draw_args = {
            k: v
            for k, v in vars(args).items()
            if k not in ["command", "shape_name", "animation", "output"]
        }

        animation = args.animation if hasattr(args, 'animation') else "instant"
        setup_canvas(command, NP, animation)
        
        output_name = args.output if hasattr(args, 'output') else None
        pts = draw_shape(draw_function, **draw_args)
    
    elif args.command == "design":
        design_number = args.design_number
        draw_function_name = f"design_{design_number}"
        
        try:
            draw_function = getattr(sys.modules['designs'], draw_function_name)
            command = draw_function_name
        
        except AttributeError:
            print(f"Error: Design '{design_number}' not found in designs module.")
            return sys.exit(1)
            
        animation = args.animation if hasattr(args, 'animation') else "instant"
        setup_canvas(command, NP, animation)
        
        output_name = args.output if hasattr(args, 'output') else None
        pts = draw_shape(draw_function)
    
    else:
        print(f"Error: Unknown command '{args.command}'.")
        return sys.exit(1)
    
    post_processing(pts, name=output_name)
    
    return sys.exit(0)


if __name__ == "__main__":
    main()