import math
import os
import trimesh
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from shapely.geometry import Polygon
from trimesh import Trimesh
from planet_data import PLANETS
from orbital_math import calculate_position, calculate_orbital_angle

# All values are in milimeters

BOX_HEIGHT = 5
BOX_WIDTH = 50
BOX_LENGTH = BOX_WIDTH

OFFSET = [0,0, BOX_HEIGHT]

SUN_RADIUS = 5

ORBIT_RING_THICKNESS = 1
ORBIT_RING_SPACE = 1
ORBIT_RING_HEIGHT = 0.2

PLANET_RADIUS = 0.85

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(SCRIPT_DIR, "assets", "fonts", "DejaVuSans.ttf")
FONT = FontProperties(fname=FONT_PATH)

def place_at(mesh: Trimesh, offset=None, height=0.0) -> Trimesh:
    mesh.apply_translation([0,0,(height/2)])

    if offset:
        mesh.apply_translation(offset)

    return mesh

def create_base()->Trimesh:
    ENGRAVED_DEPTH = 0.25
    CYLINDER_RADIUS = ORBIT_RING_THICKNESS - 0.25
    CYLINDER_TOP_ORIGN = BOX_WIDTH - CYLINDER_RADIUS
    MOVE_XAXIS = (BOX_LENGTH/2) - CYLINDER_RADIUS
    MOVE_YAXIS = (BOX_WIDTH/2) - CYLINDER_RADIUS

    origin, xaxis, yaxis = [0, 0, 0], [1, 0, 0], [0, 1, 0]
    rotate_90 = trimesh.transformations.rotation_matrix(math.radians(90), yaxis, origin)
    rotate_90_sides = trimesh.transformations.rotation_matrix(math.radians(90), xaxis, origin)
    top = [-1, 1, 0]
    bottom = [1, 1, 0]
    left = [1, -1, 0]
    right = [-1, -1, 0]

    meshes = []
    box = place_at(trimesh.creation.box(extents=[BOX_WIDTH, BOX_LENGTH, BOX_HEIGHT]), None, BOX_HEIGHT)
   

    # TODO: The following code functions mathematically, however, your printing success might vary.
    # Use the letter A as a test print before enhancing with customizable messages.

    # text_path = TextPath((0, 0), "A", size=10, prop=FONT)

    # polygons = text_path.to_polygons()

    # # convert every loop to a Polygon first
    # shapely_polys = [Polygon(p) for p in polygons]

    # # sort by area, descending -> biggest is the outer boundary
    # shapely_polys.sort(key=lambda p: p.area, reverse=True)

    # outer = shapely_polys[0]
    # holes = [list(p.exterior.coords) for p in shapely_polys[1:]]

    # letter_polygon = Polygon(outer.exterior.coords, holes)

    # text_mesh = trimesh.creation.extrude_polygon(letter_polygon, ENGRAVED_DEPTH)
    # engraved_box = box.difference(text_mesh)

    # meshes.append(engraved_box)
    meshes.append(box)

    cylinder_top = trimesh.creation.cylinder(CYLINDER_RADIUS, BOX_WIDTH)
    cylinder_top.apply_transform(rotate_90)
    cylinder_top = place_at(cylinder_top, OFFSET)
    cylinder_top.apply_translation([0, MOVE_YAXIS, 0])
    cylinder_top = cylinder_top.slice_plane([0, 0, CYLINDER_TOP_ORIGN], top, True)
    cylinder_top = cylinder_top.slice_plane([0, 0, 0], bottom, True)

    cylinder_bottom = trimesh.creation.cylinder(CYLINDER_RADIUS, BOX_WIDTH)
    cylinder_bottom.apply_transform(rotate_90)
    cylinder_bottom = place_at(cylinder_bottom, OFFSET)
    cylinder_bottom.apply_translation([0, -MOVE_YAXIS, 0])
    cylinder_bottom = cylinder_bottom.slice_plane([0, 0, CYLINDER_TOP_ORIGN], right, True)
    cylinder_bottom = cylinder_bottom.slice_plane([0, 0, 0], left, True)

    cylinder_left = trimesh.creation.cylinder(CYLINDER_RADIUS, BOX_WIDTH)
    cylinder_left.apply_transform(rotate_90_sides)
    cylinder_left = place_at(cylinder_left, OFFSET)
    cylinder_left.apply_translation([MOVE_XAXIS, 0, 0])
    cylinder_left = cylinder_left.slice_plane([0, 0, CYLINDER_TOP_ORIGN], left, True)
    cylinder_left = cylinder_left.slice_plane([0, 0, 0], bottom, True)

    cylinder_right = trimesh.creation.cylinder(CYLINDER_RADIUS, BOX_WIDTH)
    cylinder_right.apply_transform(rotate_90_sides)
    cylinder_right = place_at(cylinder_right, OFFSET)
    cylinder_right.apply_translation([-MOVE_XAXIS, 0, 0])
    cylinder_right = cylinder_right.slice_plane([0, 0, CYLINDER_TOP_ORIGN], right, True)
    cylinder_right = cylinder_right.slice_plane([0, 0, 0], top, True)

    meshes.append(cylinder_top)
    meshes.append(cylinder_bottom)
    meshes.append(cylinder_left)
    meshes.append(cylinder_right)

    return meshes

def create_sun()-> Trimesh:
    shpere = trimesh.creation.uv_sphere(SUN_RADIUS)
    hemisphere = shpere.slice_plane([0,0,0], [0,0,1], True)

    return place_at(hemisphere, OFFSET)

def create_orbit_ring(previous_outer_radius: float) -> tuple[Trimesh, float]:
    r_min = previous_outer_radius + ORBIT_RING_SPACE
    r_max = r_min + ORBIT_RING_THICKNESS

    ring = place_at(trimesh.creation.annulus(r_min, r_max, ORBIT_RING_HEIGHT), OFFSET)

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

    box_meshes = create_base()
    for mesh in box_meshes:
        meshes.append(mesh)

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