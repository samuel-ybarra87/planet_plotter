# Planet Plotter

A Python tool that calculates simplified planetary orbital positions for a given date and (eventually) exports them as a 3D-printable STL model. The model will be a physical plaque showing where the planets were on a meaningful date (birthdays, anniversaries, etc.).

## Motivation

I want to print out the planet's positions with my 3D printer for various dates for my friends and family. I could model it based on NASA data, but the calculations are too complex. Simplifying it with code is more my speed.

## Status

This project is a work in progress, built as a capstone project for [Boot.dev](https://www.boot.dev) View my profile [here](https://www.boot.dev/u/samuelybarra87)

- [x] Date input with validation
- [x] Orbital angle calculation (Simplifies to circular orbits for quicker graphing)
- [x] Plaque-relative radius calculation (rank-based spacing, not true to scale)
- [x] Cartesian coordinate conversion
- [x] 2D visulization for debuggging (matplotlib)
- [ ] 3D mesh generation
- [ ] STL export
- [ ] Multi-planet support (Currently Earth only)

## Design decisions / Simplifications

- **Circular orbits**: planets are model as moving at a constant speed around a perfect circle, rather than a true ellipse. This keeps the math simple and is visually indistinguishable at plaque scale
- **Rank-based spacing**: rather than scaling real AU distances, which would make the inner planets imperceptivly close to one another, each planet's ring is spaced evenly by its order from the sun. (Mercury=1, Venus=2, Earth=3, etc.)
- **Reference epoch**: positions are calculated relative to J2000 (January 1, 2000), using published mean logitude data as each planet's starting angle.

## How to run

### Requirements

- Python 3.x
- `matplotlib` (for the debug visualization step)

### Installation

```bash
git clone https://github.com/samuel-ybarra87/planet_plotter.git
cd planet_plotter
pip install -r requirements.txt
```

### Usage

`python main.py`

You'll be prompted for a target year, month, and day. The script will calculate Earth's orbital position on that date and display it as a 2D Plot.

## Roadmap

- Add remaining 8 planets (Pluto IS a planet!)
- Generate a 3d mesh (disk based + raised orbital rings + planet)
- Export to STL for slicing in 3D printing software

## Acknowledgements

Built as a capstone project for Boot.dev

## Contributions

Contributions are very much welcome as this is my first mesh generation program.