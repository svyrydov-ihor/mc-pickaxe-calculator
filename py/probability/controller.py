import logging
import matplotlib
logging.getLogger("matplotlib").setLevel(logging.CRITICAL)
from pyscript import document, display

from py import validators
from py.probability.calculations.precise import calculate_precise_prob
from py.probability.calculations.simulation import simulate_prob

def run_all_calculations(event):
    try:
        # input validation
        durability = validators.validate_durability()
        unbreaking_level = validators.validate_unbreaking_level()
        blocks = validators.validate_blocks()
        num_of_experiments = validators.validate_num_of_experiments()
        document.querySelector("#error_message").innerText = ""

        # precise calculations
        prob, fig = calculate_precise_prob(durability, unbreaking_level, blocks)

        document.querySelector("#precise_upper_text").innerText =\
            f"Probability of not breaking pickaxe after mining {blocks} blocks is {prob * 100:.2f}%"

        document.querySelector("#precise_chart").innerHTML = ""
        display(fig, target="precise_chart")

        document.querySelector("#precise_lower_text").innerText =\
            ("X axis: how much durability will be lost\n" +
            "Highest point of curve: the most expected durability amount to lose\n" +
            "Shaded area: probability of not breaking pickaxe after mining")

        # simulation
        prob, fig = simulate_prob(durability, unbreaking_level, blocks, num_of_experiments)

        document.querySelector("#simulation_upper_text").innerText = \
            f"Probability of not breaking pickaxe after mining {blocks} blocks is {prob * 100:.2f}%"

        document.querySelector("#simulation_chart").innerHTML = ""
        display(fig, target="simulation_chart")

        document.querySelector("#simulation_lower_text").innerText = \
            ("X axis: how much durability will be lost\n" +
             "Y axis: relative frequency (frequency / number of experiments)\n"
             "Highest bar: the most frequent durability amount to lose\n" +
             "Shaded green area: probability of not breaking pickaxe after mining")
    except Exception as e:
        error_message_element = document.querySelector("#error_message")
        error_message_element.innerText = str(e)