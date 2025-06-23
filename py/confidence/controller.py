import logging
import matplotlib
logging.getLogger("matplotlib").setLevel(logging.CRITICAL)
from pyscript import document, display

from py import validators

def run_all_calculations(event):
    try:
        # input validation
        durability = validators.validate_durability()
        unbreaking_level = validators.validate_unbreaking_level()
        confidence = validators.validate_confidence()
        num_of_experiments = validators.validate_num_of_experiments()
        document.querySelector("#error_message").innerText = ""
    except Exception as e:
        document.querySelector("#error_message").innerText = str(e)