import turtle
import argparse

from shapes.polygons_stars.regular_polygon import draw_regular_polygon
from shapes.polygons_stars.regular_star import draw_regular_star
from shapes.polygons_stars.composition_1 import draw_composition_1
from shapes.polygons_stars.composition_2 import draw_composition_2
from shapes.polygons_stars.prettygon import draw_prettygon

from shapes.designs_from_data.horse import draw_horse
from shapes.designs_from_data.lion import draw_lion
from shapes.designs_from_data.bird_fish import draw_bird_fish
from shapes.designs_from_data.smurf import draw_smurf

from shapes.folding_paper_dragons.dragon import draw_dragon

from shapes.fractal_stars.fractal_star import draw_fractal_star


def setup_canvas(command: str, NP: int):
    if command == 'dragon':
        turtle.setup(width=550, height=800)
        turtle.setworldcoordinates(0, 0, 550, 800)
        
    else:
        turtle.setup(width=NP, height=NP)
        turtle.setworldcoordinates(0, 0, NP, NP)
    
    turtle.tracer(0)

    turtle.penup()
    turtle.home()
    turtle.pendown()


def draw_shape(draw_function, *args, **kwargs):
    draw_function(*args, **kwargs)


def post_processing():
    turtle.update()
    turtle.hideturtle()
    turtle.exitonclick()

    print("Post-processing step (to be defined).")


def main():
    parser = argparse.ArgumentParser(description="Draw shapes using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Chapter 1
    # Subparser for draw_regular_polygon
    polygon_parser = subparsers.add_parser("regular_polygon", help="Draw a regular polygon.")
    polygon_parser.add_argument("--K", type=int, required=True, help="Number of sides of the polygon.")
    polygon_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_regular_star
    star_parser = subparsers.add_parser("regular_star", help="Draw a regular star.")
    star_parser.add_argument("--K", type=int, required=True, help="Number of points of the star.")
    star_parser.add_argument("--H", type=int, required=True, help="Skip points when drawing the star.")
    star_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_composition_1
    composition_1_parser = subparsers.add_parser("composition_1", help="Draw a composition of shapes.")
    composition_1_parser.add_argument("--K1", type=int, required=False, help="Number of sides of the first shape.")
    composition_1_parser.add_argument("--R1_FACTOR", type=float, required=False, help="Radius factor of the first shape.")
    composition_1_parser.add_argument("--K", type=int, required=False, help="Number of sides of the second shape.")
    composition_1_parser.add_argument("--H", type=int, required=False, help="Skip points when drawing the second shape.")
    composition_1_parser.add_argument("--R_FACTOR", type=float, required=False, help="Radius factor of the second shape.")
    composition_1_parser.add_argument("--A1", type=float, required=False, help="Initial angle.")
    composition_1_parser.add_argument("--AD", type=float, required=False, help="Angle increment.")
    composition_1_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")
    
    # Subparser for draw_composition_2
    composition_2_parser = subparsers.add_parser("composition_2", help="Draw a composition of shapes.")
    composition_2_parser.add_argument("--K1", type=int, required=False, help="Number of sides of the first shape.")
    composition_2_parser.add_argument("--N", type=int, required=False, help="Number of iterations.")
    composition_2_parser.add_argument("--K", type=int, required=False, help="Number of sides of the second shape.")
    composition_2_parser.add_argument("--H", type=int, required=False, help="Skip points when drawing the second shape.")
    composition_2_parser.add_argument("--R1_FACTOR", type=float, required=False, help="Radius factor of the first shape.")
    composition_2_parser.add_argument("--R_FACTOR", type=float, required=False, help="Radius factor of the second shape.")
    composition_2_parser.add_argument("--RR", type=float, required=False, help="Radius increment.")
    composition_2_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_prettygon
    prettygon_parser = subparsers.add_parser("prettygon", help="Draw a prettygon.")
    prettygon_parser.add_argument("--K", type=int, required=True, help="Number of sides of the prettygon.")
    prettygon_parser.add_argument("--AN", type=float, required=False, help="Angle increment.")
    prettygon_parser.add_argument("--RA", type=float, required=False, help="Radius increment.")
    prettygon_parser.add_argument("--AA", type=float, required=False, help="Initial angle.")
    prettygon_parser.add_argument("--RR", type=float, required=False, help="Initial radius.")
    prettygon_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Chapter 2
    # Subparser for draw_horse
    horse_parser = subparsers.add_parser("horse", help="Draw a horse.")
    horse_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_lion
    lion_parser = subparsers.add_parser("lion", help="Draw a lion.")
    lion_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_bird_fish
    bird_fish_parser = subparsers.add_parser("bird_fish", help="Draw a bird or a fish.")
    bird_fish_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for smurf
    smurf_parser = subparsers.add_parser("smurf", help="Draw a smurf.")
    smurf_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Chapter 3
    # Subparser for draw_dragon
    dragon_parser = subparsers.add_parser("dragon", help="Draw a dragon.")
    dragon_parser.add_argument("--N", type=int, required=False, help="Number of iterations.")
    dragon_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Chapter 4
    # Subparser for draw_fractal_star
    fractal_star_parser = subparsers.add_parser("fractal_star", help="Draw a fractal star.")
    fractal_star_parser.add_argument("--N", type=int, required=False, help="Number of iterations.")
    fractal_star_parser.add_argument("--NP", type=int, required=False, help="Canvas size (NP x NP).")


    args = parser.parse_args()

    if args.NP is None:
        args.NP = 480

    setup_canvas(args.command, args.NP)

    # Draw shape
    if args.command == "regular_polygon":
        draw_shape(draw_regular_polygon, K=args.K, NP=args.NP)
    
    elif args.command == "regular_star":
        draw_shape(draw_regular_star, K=args.K, H=args.H, NP=args.NP)

    elif args.command == "composition_1":
        draw_shape(draw_composition_1)

    elif args.command == "composition_2":
        draw_shape(draw_composition_2)

    elif args.command == "prettygon":
        draw_shape(draw_prettygon)

    elif args.command == "horse":
        draw_shape(draw_horse)
        
    elif args.command == "lion":
        draw_shape(draw_lion)
        
    elif args.command == "bird_fish":
        draw_shape(draw_bird_fish)
        
    elif args.command == "smurf":
        draw_shape(draw_smurf)
        
    elif args.command == "dragon":
        draw_shape(draw_dragon, N=args.N, NP=args.NP)
        
    elif args.command == "fractal_star":
        draw_shape(draw_fractal_star)

    # Post-processing step
    post_processing()


if __name__ == "__main__":
    main()