from typing import List
from build123d import *


def generate_cad(pts: List, name: str):
    with BuildPart() as part:
        with BuildSketch(Plane.XZ) as s:
            with BuildLine() as l:
                l1 = Polyline(*pts)
            
            trace(line_width=2.5)
        
        extrude(amount=10)

    try:
        if name:
            export_stl(part.part, f"{name}.stl")
        
        else:
            export_stl(part.part, "my_design.stl")

    except Exception as err:
        print(f"Error exporting STL: {err}")
        
    return