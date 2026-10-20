import trimesh
import os
from planet_data import PLANETS
from trimesh import Trimesh
from orbital_math import calculate_position, calculate_orbital_angle

# All values are in milimeters

BOX_HEIGHT = 5
BOX_WIDTH = 50
BOX_LENGTH = 50

SUN_RADIUS = 5
SUN_OFFSET = [0,0, BOX_HEIGHT]

ORBIT_RING_THICKNESS = 1
ORBIT_RING_SPACE = 1
ORBIT_RING_HEIGHT = 0.2
ORBIT_RING_OFFSET = [0, 0, BOX_HEIGHT]

PLANET_RADIUS = 0.85

def place_at(mesh: Trimesh, offset=None, height=0.0) -> Trimesh:
    mesh.apply_translation([0,0,(height/2)])

    if offset:
        mesh.apply_translation(offset)

    return mesh

def create_base()->Trimesh:
    meshes = []
    box = place_at(trimesh.creation.box(extents=[BOX_WIDTH, BOX_LENGTH, BOX_HEIGHT]), None, BOX_HEIGHT)
    meshes.append(box)

    base = trimesh.util.concatenate(meshes)

    return base

def create_sun()-> Trimesh:
    shpere = trimesh.creation.uv_sphere(SUN_RADIUS)
    hemisphere = shpere.slice_plane([0,0,0], [0,0,1], True)

    return place_at(hemisphere, SUN_OFFSET)

def create_orbit_ring(previous_outer_radius: float) -> tuple[Trimesh, float]:
    r_min = previous_outer_radius + ORBIT_RING_SPACE
    r_max = r_min + ORBIT_RING_THICKNESS

    ring = place_at(trimesh.creation.annulus(r_min, r_max, ORBIT_RING_HEIGHT), ORBIT_RING_OFFSET)

    return (ring, r_max)

def calculate_planet_radius(orbit_rank: int) -> float:
    r_max = orbit_rank * (ORBIT_RING_SPACE + ORBIT_RING_THICKNESS) + SUN_RADIUS

    return r_max - (ORBIT_RING_THICKNESS / 2)

def create_planet(planet_pos: tuple[float, float])-> Trimesh:
    PLANET_OFFSET = [planet_pos["x"], planet_pos["y"], BOX_HEIGHT]
    shpere = trimesh.creation.uv_sphere(PLANET_RADIUS)
    hemisphere = shpere.slice_plane([0,0,0], [0,0,1], True)

    return place_at(hemisphere, PLANET_OFFSET)

def create_plaque(OUTPUT_PATH: str, plaque_date: str, days_elapsed: int):
    meshes = []

    box = place_at(trimesh.creation.box(extents=[BOX_WIDTH, BOX_LENGTH, BOX_HEIGHT]), None, BOX_HEIGHT)
    meshes.append(box)

    sun = create_sun()
    meshes.append(sun)

    current_radius = SUN_RADIUS
    for i in range(0, 9): # There are NINE planets!
        ring, current_radius = create_orbit_ring(current_radius)
        meshes.append(ring)

    # Planet logic goes here
    for p in PLANETS:
        planet_orbit_angle = calculate_orbital_angle(p, days_elapsed)
        planet_radius = calculate_planet_radius(p.orbit_rank)
        planet_pos = calculate_position(planet_radius, planet_orbit_angle)
        planet=create_planet(planet_pos)
        meshes.append(planet)

    base_mesh = trimesh.util.concatenate(meshes)

    base_mesh.export(os.path.join(OUTPUT_PATH, f"plaque_for_{plaque_date}.stl"))