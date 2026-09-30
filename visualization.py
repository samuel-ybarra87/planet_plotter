import matplotlib.pyplot as plt

def plot_positions(positions: list[tuple[str, float, float]]):
    for name, x, y in positions:
        plt.scatter(x, y)
        plt.annotate(name, (x,y))

    plt.scatter(0, 0, color="orange") # Sol
    plt.annotate("Sun", (0,0))
    plt.gca().set_aspect("equal")
    plt.grid(True)
    plt.show()