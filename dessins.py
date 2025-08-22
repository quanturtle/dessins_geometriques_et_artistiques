"""Command-line interface for drawing geometric designs using Turtle graphics."""

import argparse
import inspect
import math
import sys
import turtle
from typing import Any, Callable, Optional, TypeVar

from cad import generate_cad
from designs import *
from shapes import *

T = TypeVar("T")


def setup_canvas(width: int, height: int, animation: str = "instant") -> None:
    """Initialize the turtle canvas."""

    turtle.setup(width=width, height=height)
    turtle.setworldcoordinates(0, 0, width, height)

    match animation:
        case "instant":
            turtle.tracer(0)
        case "fast":
            turtle.speed("fast")
        case "fastest":
            turtle.speed("fastest")

    turtle.penup()
    turtle.home()


def draw_shape(
    draw_function: Callable[..., T],
    width: int,
    height: int,
    animation: str,
    *args: Any,
    **kwargs: Any,
) -> T:
    """Draw a shape, auto-scaling it to fit the canvas."""

    # First pass to capture the bounding box
    turtle.tracer(0, 0)
    preview_pts = draw_function(*args, **kwargs)
    turtle.reset()

    if preview_pts:
        xs = [p[0] for p in preview_pts]
        ys = [p[1] for p in preview_pts]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        bbox_w = max_x - min_x or 1
        bbox_h = max_y - min_y or 1
        canvas_ratio = width / height
        bbox_ratio = bbox_w / bbox_h
        if bbox_ratio > canvas_ratio:
            bbox_h = bbox_w / canvas_ratio
        else:
            bbox_w = bbox_h * canvas_ratio
        pad = 0.05 * max(bbox_w, bbox_h)
        cx = (min_x + max_x) / 2
        cy = (min_y + max_y) / 2
        left = cx - bbox_w / 2 - pad
        right = cx + bbox_w / 2 + pad
        bottom = cy - bbox_h / 2 - pad
        top = cy + bbox_h / 2 + pad
        turtle.setworldcoordinates(left, bottom, right, top)
    else:
        turtle.setworldcoordinates(0, 0, width, height)

    match animation:
        case "instant":
            turtle.tracer(0)
        case "fast":
            turtle.speed("fast")
        case "fastest":
            turtle.speed("fastest")

    turtle.penup()
    turtle.home()

    return draw_function(*args, **kwargs)


def post_processing(pts: Optional[list[tuple[float, float]]] = None, name: Optional[str] = None) -> None:
    """Finalize drawing and optionally export CAD data."""

    turtle.hideturtle()
    turtle.update()

    if pts and name:
        generate_cad(pts, name)

    turtle.exitonclick()


def get_shape_args() -> dict[str, dict[str, Any]]:
    """Provide CLI argument specifications for available shapes."""

    return {
        "regular_polygon": {
            "help": "Draw a regular polygon.",
            "args": {
                "-K": {"type": int, "default": 5, "required": False, "help": "Number of sides"},
                "-R": {"type": float, "default": 240 * 0.45, "required": False, "help": "Radius, NP/2*R"},
                "-AD": {"type": float, "default": math.pi / 4, "required": False, "help": "Starting angle in radians"},
            },
        },
        "regular_star": {
            "help": "Draw a regular star.",
            "args": {
                "-K": {"type": int, "default": 8, "required": False, "help": "Number of points"},
                "-H": {"type": int, "default": 3, "required": False, "help": "Skip H points each time"},
                "-R": {"type": float, "default": 130, "required": False, "help": "Radius"},
                "-AD": {"type": float, "default": math.pi / 2, "required": False, "help": "Starting angle in radians"},
            },
        },
    }


def get_available_shapes() -> list[str]:
    """Return a list of available shape names."""

    shapes = []
    for name in dir(sys.modules["shapes"]):
        if name.startswith("draw_"):
            shapes.append(name[5:])  # Remove 'draw_' prefix
    return shapes


def get_available_designs() -> list[str]:
    """Return a list of available design numbers."""

    designs_list = []
    for name in dir(sys.modules["designs"]):
        if name.startswith("design_"):
            design_number = name.split("_")[1]
            designs_list.append(design_number)
    return designs_list


def initialize_parsers() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(description="Draw shapes and designs using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    common_args = {
        "--animation": {
            "choices": ["fast", "fastest", "instant"],
            "default": "instant",
            "required": False,
            "help": "Animation speed (default: instant)",
        },
        "--output": {
            "type": str,
            "default": None,
            "required": False,
            "help": "Output file name (default: No file output)",
        },
        "--width": {
            "type": int,
            "default": 480,
            "required": False,
            "help": "Canvas width (default: 480)",
        },
        "--height": {
            "type": int,
            "default": 480,
            "required": False,
            "help": "Canvas height (default: 480)",
        },
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


def main() -> int:
    """Program entry point."""

    parser = initialize_parsers()
    args = parser.parse_args()

    width = getattr(args, "width", 480)
    height = getattr(args, "height", 480)
    size = min(width, height)

    if args.command == "shape":
        shape_name = args.shape_name
        draw_function_name = f"draw_{shape_name}"

        try:
            draw_function = getattr(sys.modules["shapes"], draw_function_name)
        except AttributeError:
            print(f"Error: Shape '{shape_name}' not found in shapes module.")
            return 1

        draw_args = {
            k: v
            for k, v in vars(args).items()
            if k not in {"command", "shape_name", "animation", "output", "width", "height"}
        }

        sig = inspect.signature(draw_function)
        if "NP" in sig.parameters and "NP" not in draw_args:
            draw_args["NP"] = size

        animation = args.animation if hasattr(args, "animation") else "instant"
        setup_canvas(width, height, animation)

        output_name = args.output if hasattr(args, "output") else None
        pts = draw_shape(draw_function, width, height, animation, **draw_args)

    elif args.command == "design":
        design_number = args.design_number
        draw_function_name = f"design_{design_number}"

        try:
            draw_function = getattr(sys.modules["designs"], draw_function_name)
        except AttributeError:
            print(f"Error: Design '{design_number}' not found in designs module.")
            return 1

        animation = args.animation if hasattr(args, "animation") else "instant"
        setup_canvas(width, height, animation)

        draw_args = {}
        sig = inspect.signature(draw_function)
        if "NP" in sig.parameters:
            draw_args["NP"] = size

        output_name = args.output if hasattr(args, "output") else None
        pts = draw_shape(draw_function, width, height, animation, **draw_args)

    else:
        print(f"Error: Unknown command '{args.command}'.")
        return 1

    post_processing(pts, name=output_name)
    return 0


def test_everything(width: int = 480, height: int = 480, animation: str = "instant") -> None:
    """Draw every available design sequentially in 4x4 batches.

    Each batch renders 16 designs on the same canvas one after another,
    resetting the canvas after every group to keep resources in check.
    """

    design_numbers = sorted(int(n) for n in get_available_designs())
    size = min(width, height)

    for index, num in enumerate(design_numbers, start=1):
        draw_function = getattr(sys.modules["designs"], f"design_{num}")

        setup_canvas(width, height, animation)

        draw_args: dict[str, Any] = {}
        if "NP" in inspect.signature(draw_function).parameters:
            draw_args["NP"] = size

        draw_shape(draw_function, width, height, animation, **draw_args)
        turtle.update()

        # Reset after each design to avoid overlap
        turtle.reset()

        # Every 16 designs, clear the screen completely
        if index % 16 == 0:
            turtle.clearscreen()

    turtle.bye()


if __name__ == "__main__":
    sys.exit(main())

