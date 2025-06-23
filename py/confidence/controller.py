import logging
import matplotlib
logging.getLogger("matplotlib").setLevel(logging.CRITICAL)
from pyscript import document, display

from py import validators
from py.confidence.calculations.precise import calculate_precise_prob

def run_all_calculations(event):
    try:
        # input validation
        durability = validators.validate_durability()
        unbreaking_level = validators.validate_unbreaking_level()
        confidence = validators.validate_confidence()
        num_of_experiments = validators.validate_num_of_experiments()
        document.querySelector("#error_message").innerText = ""

        # precise calculations
        interval, fig = calculate_precise_prob(durability, unbreaking_level, confidence)

        document.querySelector("#precise_upper_text").innerText = (
            f"You can be {confidence*100}% sure that the pickaxe will mine\n" +
            f"from {interval[0]} to {interval[1]} blocks")

        document.querySelector("#precise_chart").innerHTML = ""
        display(fig, target="precise_chart")

        document.querySelector("#precise_lower_text").innerText = (
            "X axis: how much blocks will be mined\n" +
            "Highest point of curve: the most expected amount of blocks to mine\n" +
            "Left and right boundaries: the least expected amount of blocks to mine")
    except Exception as e:
        document.querySelector("#error_message").innerText = str(e)