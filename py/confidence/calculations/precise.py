import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.stats import norm

def calculate_precise_prob(durability: int, unbreaking_level: int, confidence_level: float) -> [[np.float64, np.float64], Figure]:
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