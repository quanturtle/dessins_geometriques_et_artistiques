import turtle
import argparse
from shapes.polygons_stars.regular_polygon import draw_regular_polygon
from shapes.polygons_stars.regular_star import draw_regular_star


def setup_canvas(NP: int):
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    
    turtle.penup()
    turtle.home()
    turtle.pendown()


def draw_shape(draw_function, *args, **kwargs):
    draw_function(*args, **kwargs)


def post_processing():
    turtle.hideturtle()
    turtle.exitonclick()

    print("Post-processing step (to be defined).")


def main():
    parser = argparse.ArgumentParser(description="Draw shapes using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subparser for draw_regular_polygon
    polygon_parser = subparsers.add_parser("regular_polygon", help="Draw a regular polygon.")
    polygon_parser.add_argument("--K", type=int, required=True, help="Number of sides of the polygon.")
    polygon_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_regular_star
    star_parser = subparsers.add_parser("regular_star", help="Draw a regular star.")
    star_parser.add_argument("--K", type=int, required=True, help="Number of points of the star.")
    star_parser.add_argument("--H", type=int, required=True, help="Skip points when drawing the star.")
    star_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    args = parser.parse_args()

    if args.NP is None:
        args.NP = 480

    setup_canvas(args.NP)

    # Draw shape
    if args.command == "regular_polygon":
        draw_shape(draw_regular_polygon, K=args.K, NP=args.NP)
    
    elif args.command == "regular_star":
        draw_shape(draw_regular_star, K=args.K, H=args.H, NP=args.NP)

    # Post-processing step
    post_processing()


if __name__ == "__main__":
    main()