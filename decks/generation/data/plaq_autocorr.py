import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from statsmodels.tsa.stattools import acf


def get_plaquettes(filename):
    result = []
    trajectory = None
    with open(filename) as f:
        for line in f:
            if line.startswith("[MAIN][0]Trajectory"):
                trajectory = int(line.split()[1].strip("#:."))
            if trajectory is not None and trajectory < 500:
                continue
            if trajectory is not None and trajectory > 12000:
                break
            if line.startswith("[MAIN][0]Plaquette: "):
                result.append(float(line.split()[1]))

    return result


def plot_acf(filenames, output_filename):
    plt.rcParams["text.usetex"] = True
    fig, ax = plt.subplots(layout="constrained")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$R_{PP}(\tau)$")

    for filename, label in filenames.items():
        plaquettes = get_plaquettes(filename)
        ax.plot(acf(plaquettes, nlags=1000, fft=False), label=label)

    ax.axhline(0, color="black")
    ax.xaxis.set_minor_locator(MultipleLocator(50))
    ax.grid(axis="x")
    ax.grid(axis="x", which="minor", dashes=(2, 3))
    ax.set_ylim(-0.1, 0.25)
    ax.legend(loc="best")
    fig.savefig(output_filename)
    plt.close(fig)


if __name__ == "__main__":
    plot_acf(
        {
            "out_hmc_reusedseed": "Re-seeded every 50 trajectories, seed 13813",
            "out_hmc_seedonce": "Seeded only at start of Markov chain, seed 13813"
        },
        "../images/seeding_autocorrelation.svg",
    )
