import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.stats import norm

def calculate_precise_prob(durability: int, unbreaking_level: int, blocks: int) -> [np.float64, Figure]:
    """
    Calculates probability of not breaking tool after mining specific amount of blocks
    """
    # distribution params
    dur_reduce_prob = 1 / (1 + unbreaking_level)
    mu = dur_reduce_prob * blocks
    variance = (1 - dur_reduce_prob) ** 2 * dur_reduce_prob + dur_reduce_prob ** 2 * (1 - dur_reduce_prob)
    std = np.sqrt(blocks) * np.sqrt(variance)

    # normal curve chart
    def normal_curve(x_in):
        return norm.pdf(x_in, loc=mu, scale=std)

    x_min = mu - 4 * std
    x_max = mu + 4 * std
    x = np.linspace(x_min, x_max, 100)
    y = normal_curve(x)
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot(x, y, color="b")
    ax.plot([x_min, x_max], [0, 0], color="b")

    # area under the curve
    ax.fill_between(x, y, where=(x < durability), facecolor="g", alpha=0.4)
    area = norm.cdf(durability, loc=mu, scale=std)

    # peak
    peak = normal_curve(mu)
    ax.plot([mu, mu], [peak, 0], linestyle="--", color="r", marker="o")
    ax.annotate(f"{mu:.0f}", xy=(mu, peak), fontsize=12, color="r")
    fig.tight_layout()

    return [area, fig]