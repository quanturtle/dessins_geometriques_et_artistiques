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
    design_33
)

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
    turtle.hideturtle()
    turtle.update()
    turtle.exitonclick()

    print("Post-processing step (to be defined).")


def main():
    parser = argparse.ArgumentParser(description="Draw shapes using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Chapter 1
    # Subparser for draw_regular_polygon
    polygon_parser = subparsers.add_parser("regular_polygon", help="Draw a regular polygon.")
    polygon_parser.add_argument("-K", type=int, required=False, help="Number of sides of the polygon.")
    polygon_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_regular_star
    star_parser = subparsers.add_parser("regular_star", help="Draw a regular star.")
    star_parser.add_argument("-K", type=int, required=False, help="Number of points of the star.")
    star_parser.add_argument("-H", type=int, required=False, help="Skip points when drawing the star.")
    star_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_composition_1
    composition_1_parser = subparsers.add_parser("composition_1", help="Draw a composition of shapes.")
    composition_1_parser.add_argument("-K1", type=int, required=False, help="Number of sides of the first shape.")
    composition_1_parser.add_argument("-R1_FACTOR", type=float, required=False, help="Radius factor of the first shape.")
    composition_1_parser.add_argument("-K", type=int, required=False, help="Number of sides of the second shape.")
    composition_1_parser.add_argument("-H", type=int, required=False, help="Skip points when drawing the second shape.")
    composition_1_parser.add_argument("-R_FACTOR", type=float, required=False, help="Radius factor of the second shape.")
    composition_1_parser.add_argument("-A1", type=float, required=False, help="Initial angle.")
    composition_1_parser.add_argument("-AD", type=float, required=False, help="Angle increment.")
    composition_1_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")
    
    # Subparser for draw_composition_2
    composition_2_parser = subparsers.add_parser("composition_2", help="Draw a composition of shapes.")
    composition_2_parser.add_argument("-K1", type=int, required=False, help="Number of sides of the first shape.")
    composition_2_parser.add_argument("-N", type=int, required=False, help="Number of iterations.")
    composition_2_parser.add_argument("-K", type=int, required=False, help="Number of sides of the second shape.")
    composition_2_parser.add_argument("-H", type=int, required=False, help="Skip points when drawing the second shape.")
    composition_2_parser.add_argument("-R1_FACTOR", type=float, required=False, help="Radius factor of the first shape.")
    composition_2_parser.add_argument("-R_FACTOR", type=float, required=False, help="Radius factor of the second shape.")
    composition_2_parser.add_argument("-RR", type=float, required=False, help="Radius increment.")
    composition_2_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_prettygon
    prettygon_parser = subparsers.add_parser("prettygon", help="Draw a prettygon.")
    prettygon_parser.add_argument("-K", type=int, required=False, help="Number of sides of the prettygon.")
    prettygon_parser.add_argument("-AN", type=float, required=False, help="Angle increment.")
    prettygon_parser.add_argument("-RA", type=float, required=False, help="Radius increment.")
    prettygon_parser.add_argument("-AA", type=float, required=False, help="Initial angle.")
    prettygon_parser.add_argument("-RR", type=float, required=False, help="Initial radius.")
    prettygon_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Chapter 2
    # Subparser for draw_horse
    horse_parser = subparsers.add_parser("horse", help="Draw a horse.")
    horse_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_lion
    lion_parser = subparsers.add_parser("lion", help="Draw a lion.")
    lion_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for draw_bird_fish
    bird_fish_parser = subparsers.add_parser("bird_fish", help="Draw a bird or a fish.")
    bird_fish_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Subparser for smurf
    smurf_parser = subparsers.add_parser("smurf", help="Draw a smurf.")
    smurf_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Chapter 3
    # Subparser for draw_dragon
    dragon_parser = subparsers.add_parser("dragon", help="Draw a dragon.")
    dragon_parser.add_argument("-N", type=int, required=False, help="Number of iterations.")
    dragon_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    # Chapter 4
    # Subparser for draw_fractal_star
    fractal_star_parser = subparsers.add_parser("fractal_star", help="Draw a fractal star.")
    fractal_star_parser.add_argument("-N", type=int, required=False, help="Number of iterations.")
    fractal_star_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")
    
    # design subparser
    design_parser = subparsers.add_parser("design", help="Draw a design.")
    design_parser.add_argument("-N", type=int, required=False, help="Design number.")
    design_parser.add_argument("-NP", type=int, required=False, help="Canvas size (NP x NP).")

    args = parser.parse_args()

    if args.NP is None:
        args.NP = 480

    setup_canvas(args.command, args.NP)

    # Draw shape
    if args.command == "regular_polygon":
        draw_shape(draw_regular_polygon)
    
    elif args.command == "regular_star":
        draw_shape(draw_regular_star)

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
        draw_shape(draw_dragon)
        
    elif args.command == "fractal_star":
        draw_shape(draw_fractal_star)
        
    elif args.command == "design":
        design_33()

    # Post-processing step
    post_processing()


if __name__ == "__main__":
    main()