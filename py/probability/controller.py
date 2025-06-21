from pyscript import document
import validators

def run_all_calculations(event):
    try:
        durability = validators.validate_durability()
        unbreaking_level = validators.validate_unbreaking_level()
        blocks = validators.validate_blocks()
        num_of_experiments = validators.validate_num_of_experiments()
        error_message_element = document.querySelector("#error_message")
        error_message_element.innerText = ""

    except ValueError as e:
        error_message_element = document.querySelector("#error_message")
        error_message_element.innerText = e