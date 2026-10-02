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
- [x] 2D visulization for debugging (matplotlib)
- [x] 3D mesh generation and file export (renders test STL file and exports to user's desired directory)
- [ ] 3D mesh generation (Full design of Sun and orbit ring with planet marker)
- [ ] Multi-planet support (Currently Earth only)

## Design decisions / Simplifications

- **Circular orbits**: planets are model as moving at a constant speed around a perfect circle, rather than a true ellipse. This keeps the math simple and is visually indistinguishable at plaque scale
- **Rank-based spacing**: rather than scaling real AU distances, which would make the inner planets imperceptivly close to one another, each planet's ring is spaced evenly by its order from the sun. (Mercury=1, Venus=2, Earth=3, etc.)
- **Reference epoch**: positions are calculated relative to J2000 (January 1, 2000), using published mean logitude data as each planet's starting angle.

## Output handling

The script prompts for an output folder path at startup. It works with both native Linux/macOS paths and Windows paths accessed through WSL (e.g. `/mnt/c/Users/yourname/Documents`). If the folder doesn't exist, you'll be asked whether to create it. Leaving the prompt blank saves the STL file in the current working directory.

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

- Generate the full plaque mesh (disk base + raised orbital rings + planet markers)
- Add the remaining planets (Pluto IS a planet!)
- Multi-planet rendering in both the 2D visualization and the 3D mesh

## Acknowledgements

Built as a capstone project for Boot.dev

## Contributions

Contributions are very much welcome as this is my first mesh generation program.