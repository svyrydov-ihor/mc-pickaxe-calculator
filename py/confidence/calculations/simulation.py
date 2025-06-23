import random
from typing import Dict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def simulate_prob(durability: int, unbreaking_level: int, confidence_level: float, num_of_experiments: int) -> [[np.float64, np.float64], Figure]:
    # setup
    dur_reduce_prob = 1 / (1 + unbreaking_level)
    outcomes: Dict[int, int] = {} # key: blocks mined, value: frequency
    max_blocks_to_mine = int(1 / dur_reduce_prob * durability * 10) # upper bound for blocks to mine, avoiding infinite mining
                                                                    # 10 stds away from expected value
    # running simulations
    for n in range(num_of_experiments):
        curr_durability = durability
        blocks_mined = 0
        for i in range(1, max_blocks_to_mine):
            if random.random() <= dur_reduce_prob:
                curr_durability -= 1
            if curr_durability == 0:
                blocks_mined = i

        if outcomes.keys().__contains__(blocks_mined):
            outcomes[blocks_mined] += 1
        else:
            outcomes[blocks_mined] = 1

    # chart and confidence interval
    outcomes_sorted = sorted(outcomes.items())
    x = []
    y = []
    colors = []
    cumulative_area = 0
    alpha = 1 - confidence_level
    left_area = alpha / 2
    median_x = -1
    median_y = -1
    for item in outcomes_sorted:
        x.append(item[0])
        relative_frequency =  item[1] / num_of_experiments
        y.append(relative_frequency)
        cumulative_area += relative_frequency
        if cumulative_area <= left_area or cumulative_area >= confidence_level + left_area:
            colors.append("b")
        else:
            colors.append("g")
        if median_x == -1 and cumulative_area >= 0.5:
            median_x = item[0]
            median_y = relative_frequency

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.bar(x, y, color=colors, alpha=0.4)

    # median
    ax.plot([median_x, median_x], [median_y, 0], linestyle="--", color="r", marker="o")
    ax.annotate(f"{median_x}", xy=(median_x, median_y), fontsize=12, color="r")

    # borders
    if colors.count("g") < 1:
        fig.tight_layout()
        return [[median_x, median_x], fig]

    left_index = colors.index("g")
    left_x = x[left_index]
    left_y = y[left_index]
    for i in range(len(colors)-1, left_index-1, -1):
        if colors[i] == "g":
            right_x = x[i]
            right_y = y[i]
            break
    for x, y in zip([left_x, right_x], [left_y, right_y]):
        ax.plot([x, x],
                [y, 0], linestyle="--", color="r", marker="o")
        ax.annotate(f"{x}", xy=(x, y), fontsize=12, color="r")

    fig.tight_layout()

    return [[left_x, right_x], fig]