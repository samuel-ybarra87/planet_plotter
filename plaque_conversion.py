def calculate_plaque_radius(orbit_rank: int, sun_radius=1.5, ring_spacing=1.0) -> float:
    return sun_radius + orbit_rank * ring_spacing