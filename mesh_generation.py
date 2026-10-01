import trimesh
import os

def create_plaque(OUTPUT_PATH: str, plaque_date: str, plaque_data=None):
    disc = trimesh.creation.cylinder(radius=1.5, height=0.2)
    disc.export(os.path.join(OUTPUT_PATH, f"test_disc_{plaque_date}.stl"))