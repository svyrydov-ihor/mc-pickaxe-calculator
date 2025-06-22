import random
from typing import Dict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def simulate_prob(durability: int, unbreaking_level: int, blocks: int, num_of_experiments: int) -> [np.float64, Figure]:
    """
    Approximates the probability of a tool not breaking after a number of mined blocks.

    This function runs a Monte Carlo simulation in order to estimate the durability loss.
    It runs specified amount of simulations. More experiments results in higher accuracy.

    Args:
        durability: The starting durability of the tool.
        unbreaking_level: The level of the Unbreaking enchantment.
        blocks: The number of blocks to be mined, representing the number of tool uses.
        num_of_experiments: The number of experiments to be simulated.

    Returns:
        list: A list containing:
            - np.float64: The probability (from 0.0 to 1.0) that the tool will not break.
            - Figure: A matplotlib Figure object visualizing the distribution of durability loss.
    """
    # setup
    dur_reduce_prob = 1 / (1 + unbreaking_level)
    outcomes: Dict[int, int] = {} # key: durability loss, value: frequency

    # running simulations
    for n in range(num_of_experiments):
        curr_durability = durability
        for i in range(blocks):
            if random.random() <= dur_reduce_prob:
                curr_durability -= 1
        loss = durability - curr_durability
        if outcomes.keys().__contains__(loss):
            outcomes[loss] += 1
        else:
            outcomes[loss] = 1

    # chart and area
    outcomes_sorted = sorted(outcomes.items())
    x = []
    y = []
    colors = []
    area = 0
    for item in outcomes_sorted:
        x.append(item[0])
        relative_frequency =  item[1] / num_of_experiments
        y.append(relative_frequency)
        if item[0] <= durability:
            colors.append("g")
            area += relative_frequency
        else:
            colors.append("b")

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.bar(x, y, color=colors, alpha=0.4)

    # peak
    peak_y = max(y)
    peak_index = y.index(peak_y)
    peak_x = x[peak_index]
    ax.plot([peak_x, peak_x], [peak_y, 0], linestyle="--", color="r", marker="o")
    ax.annotate(f"{peak_x}", xy=(peak_x, peak_y), fontsize=12, color="r")

    fig.tight_layout()

    return [area, fig]