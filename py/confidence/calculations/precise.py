import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.stats import norm

def calculate_precise_conf(durability: int, unbreaking_level: int, confidence_level: float) -> [[np.float64, np.float64], Figure]:
    """
    Approximates confidence interval for an amount of blocks that pickaxe can mine.

    This function models the discrete geometric distribution of an amount of blocks
    that pickaxe can mine as a continuous normal distribution. It calculates the mean
    and standard deviation for an amount of blocks based on Unbreaking enchantment level
    and durability amount. Then the specified confidence level is applied in order to return
    confidence interval.

    Args:
        durability: The starting durability of the tool.
        unbreaking_level: The level of the Unbreaking enchantment.
        confidence_level: The confidence level for the confidence interval (from 0.0 to 1.0).

    Returns:
        list: A list containing:
            - list[np.float64, np.float64]: The confidence interval which specifies the amount
            of blocks that pickaxe can mine.
            - Figure: A matplotlib Figure object visualizing the distribution of the amount of blocks.
    """
    # distribution params
    dur_reduce_prob = 1 / (1 + unbreaking_level)
    mu = 1 / dur_reduce_prob * durability
    variance = (1 - dur_reduce_prob) / dur_reduce_prob ** 2
    std = np.sqrt(durability) * np.sqrt(variance)

    # normal curve plot
    def normal_curve(x_in):
        return norm.pdf(x_in, loc=mu, scale=std)

    x = np.linspace(mu - 4 * std, mu + 4 * std, 500)
    y = normal_curve(x)
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, color="b")

    # confidence interval
    alpha = 1 - confidence_level
    cumulative_probability = 1 - (alpha / 2)
    z_score = norm.ppf(cumulative_probability)
    lower = mu - z_score * std
    upper = mu + z_score * std
    ax.fill_between(x, y, where=(lower <= x) & (x <= upper), color="g", alpha=0.4)

    # borders
    x_lines = [lower, mu, upper]
    y_lines =normal_curve(x_lines)
    for x, y in zip(x_lines, y_lines):
        ax.plot([x, x],
                [y, 0], linestyle="--", color="r", marker="o")
        ax.annotate(f"{x:.0f}", xy=(x, y), fontsize=12, color="r")

    fig.tight_layout()

    return [[lower, upper], fig]