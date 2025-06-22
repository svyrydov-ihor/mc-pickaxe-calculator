import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.stats import norm

def calculate_precise_prob(durability: int, unbreaking_level: int, blocks: int) -> [np.float64, Figure]:
    """
    Approximates the probability of a tool not breaking after a number of mined blocks.

    This function models the discrete binomial distribution of durability loss as a
    continuous normal distribution. It calculates the mean and standard deviation
    for durability loss based on Unbreaking enchantment level and the amount of blocks mined.

    Args:
        durability: The starting durability of the tool.
        unbreaking_level: The level of the Unbreaking enchantment.
        blocks: The number of blocks to be mined, representing the number of tool uses.

    Returns:
        list: A list containing:
            - np.float64: The probability (from 0.0 to 1.0) that the tool will not break.
            - Figure: A matplotlib Figure object visualizing the distribution of durability loss.
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