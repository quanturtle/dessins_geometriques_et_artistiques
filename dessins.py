"""Command-line interface for drawing geometric designs using Turtle graphics."""

import argparse
import importlib
import inspect
import math
import sys
import turtle
import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def setup_canvas(command: str, width: int, height: int, animation: str = "instant") -> None:
    """Configure the turtle canvas for a given command."""
    turtle.setup(width=width, height=height)
    turtle.screensize(canvwidth=width, canvheight=height)

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
    turtle.hideturtle()


def draw_shape(draw_function: Callable[..., T], *args: Any, **kwargs: Any) -> T:
    """Invoke a drawing function with given arguments."""
    return draw_function(*args, **kwargs)


def fit_canvas_to_points(points: list[tuple[float, float]] | None) -> None:
    """Resize and center the canvas around the drawn points.

    If ``points`` is ``None`` the bounding box is derived from the Tkinter
    canvas, allowing shapes that don't return point lists to be fitted.
    """

    if points:
        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
    else:
        canvas = turtle.getcanvas()
        bbox = canvas.bbox("all")
        if not bbox:
            return
        min_cx, min_cy, max_cx, max_cy = bbox

        width = turtle.window_width()
        height = turtle.window_height()
        min_x = min_cx - width / 2
        max_x = max_cx - width / 2
        min_y = height / 2 - max_cy
        max_y = height / 2 - min_cy

    pad_x = (max_x - min_x) * 0.05 or 10
    pad_y = (max_y - min_y) * 0.05 or 10

    turtle.setworldcoordinates(
        min_x - pad_x,
        min_y - pad_y,
        max_x + pad_x,
        max_y + pad_y,
    )


def post_processing(pts: list[tuple[float, float]] | None = None, name: str | None = None) -> None:
    """Finalize drawing and optionally export CAD data."""
    turtle.hideturtle()
    turtle.update()

    if pts and name:
        try:
            from cad import generate_cad

            generate_cad(pts, name)
        except Exception as exc:  # pragma: no cover - fallback when CAD libs missing
            print(f"CAD export failed: {exc}")

    turtle.exitonclick()


def get_shape_args() -> dict[str, dict[str, Any]]:
    """Provide CLI argument specifications for available shapes."""
    return {
        "regular_polygon": {
            "help": "Draw a regular polygon.",
            "args": {
                "-K": {"type": int, "default": 5, "required": False, "help": "Number of sides"},
                "-R": {"type": float, "default": 240 * 0.45, "required": False, "help": "Radius, NP/2*R"},
                "-AD": {
                    "type": float,
                    "default": math.pi / 4,
                    "required": False,
                    "help": "Starting angle in radians",
                },
            },
        },
        "regular_star": {
            "help": "Draw a regular star.",
            "args": {
                "-K": {"type": int, "default": 8, "required": False, "help": "Number of points"},
                "-H": {
                    "type": int,
                    "default": 3,
                    "required": False,
                    "help": "Skip H points each time",
                },
                "-R": {"type": float, "default": 130, "required": False, "help": "Radius"},
                "-AD": {
                    "type": float,
                    "default": math.pi / 2,
                    "required": False,
                    "help": "Starting angle in radians",
                },
            },
        },
        "bird_fish": {
            "help": "Draw the bird-fish curve.",
            "args": {
                "-NP": {
                    "type": int,
                    "default": 480,
                    "required": False,
                    "help": "Canvas scale",
                }
            },
        },
        "complete_bipartite_graph": {
            "help": "Draw a complete bipartite graph.",
            "args": {
                "-N": {"type": int, "default": 10, "required": False, "help": "Points per set"},
                "-XA": {"type": int, "default": 0, "required": False, "help": "XA"},
                "-YA": {"type": int, "default": 0, "required": False, "help": "YA"},
                "-XB": {"type": int, "default": 0, "required": False, "help": "XB"},
                "-YB": {"type": int, "default": 480, "required": False, "help": "YB"},
                "-XC": {"type": int, "default": 480, "required": False, "help": "XC"},
                "-YC": {"type": int, "default": 0, "required": False, "help": "YC"},
                "-XD": {"type": int, "default": 480, "required": False, "help": "XD"},
                "-YD": {"type": int, "default": 480, "required": False, "help": "YD"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "composition_1": {
            "help": "Draw composition 1.",
            "args": {
                "-K1": {"type": int, "default": 5, "required": False, "help": "Inner polygon sides"},
                "-DX": {"type": float, "default": 240, "required": False, "help": "Center X"},
                "-DY": {"type": float, "default": 240, "required": False, "help": "Center Y"},
                "-R1": {
                    "type": float,
                    "default": 240 * 0.54,
                    "required": False,
                    "help": "Inner radius",
                },
                "-A1": {
                    "type": float,
                    "default": math.pi / 2,
                    "required": False,
                    "help": "Inner angle",
                },
                "-K": {"type": int, "default": 25, "required": False, "help": "Star points"},
                "-H": {"type": int, "default": 12, "required": False, "help": "Skip points"},
                "-R": {
                    "type": float,
                    "default": 240 * 0.44,
                    "required": False,
                    "help": "Outer radius",
                },
                "-AD": {
                    "type": float,
                    "default": math.pi / 2,
                    "required": False,
                    "help": "Starting angle",
                },
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "composition_2": {
            "help": "Draw composition 2.",
            "args": {
                "-K1": {"type": int, "default": 8, "required": False, "help": "Inner polygon sides"},
                "-N": {"type": int, "default": 32, "required": False, "help": "Points"},
                "-K": {"type": int, "default": 16, "required": False, "help": "Star points"},
                "-H": {"type": int, "default": 5, "required": False, "help": "Skip points"},
                "-R1": {"type": float, "default": 240 * 0.72, "required": False, "help": "Inner radius"},
                "-R": {"type": float, "default": 240 * 0.28, "required": False, "help": "Outer radius"},
                "-RR": {"type": float, "default": 0.9, "required": False, "help": "Radius ratio"},
                "-DX": {"type": float, "default": 240, "required": False, "help": "Center X"},
                "-DY": {"type": float, "default": 240, "required": False, "help": "Center Y"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "d3cube": {"help": "Draw a 3D cube.", "args": {}},
        "d3data": {
            "help": "Draw 3D data.",
            "args": {
                "-DC": {"type": int, "default": 2, "required": False, "help": "Data columns"},
                "-TC": {"type": int, "default": 2, "required": False, "help": "Time columns"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "d3structures": {"help": "Draw 3D structures.", "args": {}},
        "dragon": {
            "help": "Draw a paper-folding dragon.",
            "args": {
                "-N": {"type": int, "default": 10, "required": False, "help": "Iterations"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "elastic_grid": {
            "help": "Draw an elastic grid.",
            "args": {
                "-L_RANGE": {"type": int, "default": 2, "required": False, "help": "L range"},
                "-I_RANGE": {"type": int, "default": 21, "required": False, "help": "I range"},
                "-J_RANGE": {"type": int, "default": 21, "required": False, "help": "J range"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "fractal_star": {
            "help": "Draw a fractal star.",
            "args": {
                "-N": {"type": int, "default": 5, "required": False, "help": "Branches"},
                "-K": {"type": int, "default": 5, "required": False, "help": "Levels"},
                "-RA": {"type": float, "default": 0.35, "required": False, "help": "Ratio"},
                "-LL": {"type": int, "default": None, "required": False, "help": "Initial length"},
                "-AA": {
                    "type": float,
                    "default": 4 * math.pi / 5,
                    "required": False,
                    "help": "Angle increment",
                },
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "horse": {
            "help": "Draw a horse from data.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"}
            },
        },
        "linear_modulo": {
            "help": "Draw linear modulo patterns.",
            "args": {
                "-N": {"type": int, "default": 400, "required": False, "help": "Points"},
                "-M": {"type": int, "default": 400, "required": False, "help": "Modulo"},
                "-K1": {"type": float, "default": 4, "required": False, "help": "K1"},
                "-K2": {"type": float, "default": 5, "required": False, "help": "K2"},
                "-H": {"type": int, "default": 2, "required": False, "help": "H"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "linear_sticks": {
            "help": "Draw linear sticks patterns.",
            "args": {
                "-N": {"type": int, "default": 100, "required": False, "help": "Number of sticks"},
                "-M": {"type": int, "default": 1, "required": False, "help": "M"},
                "-K": {"type": int, "default": 5, "required": False, "help": "K"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "lion": {
            "help": "Draw a lion from data.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"}
            },
        },
        "orbiting_curves": {
            "help": "Draw orbiting curves.",
            "args": {
                "-N": {"type": int, "default": 2000, "required": False, "help": "Iterations"},
                "-T1": {"type": int, "default": 2, "required": False, "help": "T1"},
                "-T2": {"type": int, "default": 100, "required": False, "help": "T2"},
                "-K1": {"type": int, "default": 1, "required": False, "help": "K1"},
                "-K2": {"type": int, "default": 1, "required": False, "help": "K2"},
                "-R1": {"type": float, "default": 120.0, "required": False, "help": "Radius"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "prettygon": {
            "help": "Draw a prettygon.",
            "args": {
                "-K": {"type": int, "default": 200, "required": False, "help": "Iterations"},
                "-AN": {
                    "type": float,
                    "default": 1.5201254775434483,
                    "required": False,
                    "help": "Angle",
                },
                "-RA": {"type": float, "default": 0.98, "required": False, "help": "Radius ratio"},
                "-AA": {"type": float, "default": 0.0, "required": False, "help": "Angle adjust"},
                "-RR": {"type": float, "default": 384.0, "required": False, "help": "Radius"},
                "-INITIAL_Y": {
                    "type": float,
                    "default": 0,
                    "required": False,
                    "help": "Initial Y position",
                },
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "rotating_curves": {
            "help": "Draw rotating curves.",
            "args": {
                "-N": {"type": int, "default": 2000, "required": False, "help": "Iterations"},
                "-T1": {"type": int, "default": 1, "required": False, "help": "T1"},
                "-T2": {"type": int, "default": 100, "required": False, "help": "T2"},
                "-K1": {"type": int, "default": 1, "required": False, "help": "K1"},
                "-K2": {"type": int, "default": 1, "required": False, "help": "K2"},
                "-H1": {"type": int, "default": 1, "required": False, "help": "H1"},
                "-H2": {"type": int, "default": 1, "required": False, "help": "H2"},
                "-R1": {"type": float, "default": 80.0, "required": False, "help": "Radius 1"},
                "-R2": {"type": float, "default": 120.0, "required": False, "help": "Radius 2"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "simple_fractal": {
            "help": "Draw a simple fractal.",
            "args": {
                "-M": {"type": int, "default": 3, "required": False, "help": "M"},
                "-N": {"type": int, "default": 4, "required": False, "help": "N"},
                "-K": {"type": int, "default": 4, "required": False, "help": "K"},
            },
        },
        "simple_fractal_deformed": {
            "help": "Draw a deformed simple fractal.",
            "args": {
                "-M": {"type": int, "default": 3, "required": False, "help": "M"},
                "-N": {"type": int, "default": 4, "required": False, "help": "N"},
                "-K": {"type": int, "default": 4, "required": False, "help": "K"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "simple_fractal_rounded": {
            "help": "Draw a rounded simple fractal.",
            "args": {
                "-M": {"type": int, "default": 1, "required": False, "help": "M"},
                "-N": {"type": int, "default": 7, "required": False, "help": "N"},
                "-K": {"type": int, "default": 2, "required": False, "help": "K"},
                "-S": {"type": int, "default": 5, "required": False, "help": "S"},
            },
        },
        "smurf": {
            "help": "Draw a smurf from data.",
            "args": {
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"}
            },
        },
        "spiraling_curves": {
            "help": "Draw spiraling curves.",
            "args": {
                "-N": {"type": int, "default": 2000, "required": False, "help": "Iterations"},
                "-T": {"type": float, "default": 40, "required": False, "help": "T"},
                "-R": {"type": float, "default": 0.8, "required": False, "help": "Radius"},
                "-L": {"type": float, "default": 0.1, "required": False, "help": "L"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
        "surface": {
            "help": "Draw a surface.",
            "args": {
                "-N": {"type": int, "default": 6, "required": False, "help": "Grid size"},
                "-PA": {"type": float, "default": None, "required": False, "help": "Perspective angle"},
                "-E1": {"type": int, "default": 2, "required": False, "help": "Exponent 1"},
                "-E2": {"type": int, "default": 1, "required": False, "help": "Exponent 2"},
                "-E3": {"type": int, "default": 0, "required": False, "help": "Exponent 3"},
                "-NP": {"type": int, "default": 480, "required": False, "help": "Canvas scale"},
            },
        },
    }


def get_available_shapes() -> list[str]:
    """Return a list of available shape names."""
    shapes_module = importlib.import_module("shapes")
    return [name[5:] for name in dir(shapes_module) if name.startswith("draw_")]


def get_available_designs() -> list[str]:
    """Return a list of available design numbers."""
    designs_module = importlib.import_module("designs")
    designs_list: list[str] = []
    for name in dir(designs_module):
        if name.startswith("design_"):
            designs_list.append(name.split("_")[1])
    return designs_list


def print_shape_help(shape_name: str) -> None:
    """Display available parameters for a given shape."""
    shapes_module = importlib.import_module("shapes")
    func_name = f"draw_{shape_name}"
    try:
        draw_func = getattr(shapes_module, func_name)
    except AttributeError:
        print(f"Error: Shape '{shape_name}' not found.")
        return

    sig = inspect.signature(draw_func)
    doc = inspect.getdoc(draw_func) or ""

    print(f"Parameters for shape '{shape_name}':")
    if doc:
        print(doc)

    if not sig.parameters:
        print("  (no parameters)")
        return

    for name, param in sig.parameters.items():
        if param.kind in {inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD}:
            continue
        if param.default is inspect._empty:
            default = "required"
        else:
            default = f"default={param.default!r}"
        print(f"  {name}: {default}")


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
    subparsers.add_parser("help", help="List available shapes and designs")

    test_parser = subparsers.add_parser(
        "test", help="Draw all designs sequentially with a short pause"
    )
    for arg_name, arg_config in common_args.items():
        test_parser.add_argument(arg_name, **arg_config)

    return parser


def main() -> int:
    """Program entry point."""
    args_list = sys.argv[1:]
    available_shapes = set(get_available_shapes())
    output_name: str | None = None
    pts: list[tuple[float, float]] | None = None

    if args_list:
        if args_list[0] == "shape":
            if len(args_list) == 1 or args_list[1] == "help":
                print("Available shapes:")
                for name in sorted(available_shapes):
                    print(f" - {name}")
                return 0
            if args_list[-1] == "help" and args_list[1] in available_shapes:
                print_shape_help(args_list[1])
                return 0
        elif args_list[-1] == "help" and args_list[0] in available_shapes:
            print_shape_help(args_list[0])
            return 0

    parser = initialize_parsers()
    args = parser.parse_args()

    width = getattr(args, "width", 480)
    height = getattr(args, "height", 480)
    size = min(width, height)

    if args.command == "help":
        print("Commands:")
        print("  shape <shape_name> [options]   Draw a predefined shape")
        print("  design <number> [options]      Draw a predefined design")
        print("  test [options]                 Render designs in 4x4 batches")
        print("  help                           Show this help message\n")

        print("Available shapes:")
        for name in sorted(get_available_shapes()):
            print(f" - {name}")
        designs = get_available_designs()
        print(f"\nAvailable designs: 1 to {len(designs)}")
        return 0
    elif args.command == "shape":
        shape_name = args.shape_name
        draw_function_name = f"draw_{shape_name}"

        try:
            shapes_module = importlib.import_module("shapes")
            draw_function = getattr(shapes_module, draw_function_name)
            command = shape_name
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
        setup_canvas(command, width, height, animation)

        output_name = args.output if hasattr(args, "output") else None
        pts = draw_shape(draw_function, **draw_args)
        fit_canvas_to_points(pts)
        turtle.update()

    elif args.command == "design":
        design_number = args.design_number
        draw_function_name = f"design_{design_number}"

        try:
            designs_module = importlib.import_module("designs")
            draw_function = getattr(designs_module, draw_function_name)
            command = draw_function_name
        except AttributeError:
            print(f"Error: Design '{design_number}' not found in designs module.")
            return 1

        animation = args.animation if hasattr(args, "animation") else "instant"
        setup_canvas(command, width, height, animation)

        draw_args: dict[str, Any] = {}
        sig = inspect.signature(draw_function)
        if "NP" in sig.parameters:
            draw_args["NP"] = size

        output_name = args.output if hasattr(args, "output") else None
        pts = draw_shape(draw_function, **draw_args)
        fit_canvas_to_points(pts)
        turtle.update()
    elif args.command == "test":
        animation = args.animation if hasattr(args, "animation") else "instant"
        test_everything(width=width, height=height, animation=animation)
        return 0
    else:
        print(f"Error: Unknown command '{args.command}'.")
        return 1

    post_processing(pts, name=output_name)
    return 0


def test_everything(width: int = 480, height: int = 480, animation: str = "instant") -> None:
    """Draw every available design in 4x4 grid batches.

    Sixteen designs are shown at a time. Each design is scaled to fit a
    cell in the grid and placed so the batch fills the window. A short
    pause follows each drawing and between batches for visibility.
    """

    design_numbers = sorted(int(n) for n in get_available_designs())
    cell_w = width / 4
    cell_h = height / 4
    size = min(cell_w, cell_h) * 0.9

    for batch_start in range(0, len(design_numbers), 16):
        setup_canvas("test", width, height, animation)
        for idx in range(16):
            if batch_start + idx >= len(design_numbers):
                break

            num = design_numbers[batch_start + idx]
            command = f"design_{num}"
            designs_module = importlib.import_module("designs")
            draw_function = getattr(designs_module, command)

            row, col = divmod(idx, 4)
            x = -width / 2 + (col + 0.5) * cell_w
            y = height / 2 - (row + 0.5) * cell_h

            turtle.penup()
            turtle.goto(x, y)
            turtle.setheading(0)
            turtle.pendown()

            draw_args: dict[str, Any] = {}
            if "NP" in inspect.signature(draw_function).parameters:
                draw_args["NP"] = size

            draw_shape(draw_function, **draw_args)
            turtle.hideturtle()
            turtle.update()
            time.sleep(0.5)

        time.sleep(0.5)
        turtle.clearscreen()

    turtle.bye()


if __name__ == "__main__":
    sys.exit(main())
