from pyscript import document

def validate_durability() -> int:
    durability_in_element = document.querySelector("#durability_input")
    try:
        durability = int(durability_in_element.value)
        if durability <= 0:
            raise ValueError
        return durability
    except ValueError:
        raise ValueError("Durability must be a positive integer")

def validate_unbreaking_level() -> int:
    unbreaking_level_element = document.querySelector("#unbreaking_input")
    try:
        unbreaking_level = int(unbreaking_level_element.value)
        if unbreaking_level not in [1, 2, 3]:
            raise ValueError
        return unbreaking_level
    except ValueError:
        raise ValueError("Unbreaking level must be a positive integer from 1 and 3")

def validate_blocks() -> int:
    blocks_input_element = document.querySelector("#blocks_input")
    try:
        blocks = int(blocks_input_element.value)
        if blocks <= 0:
            raise ValueError
        return blocks
    except ValueError:
        raise ValueError("Blocks number must be a positive integer")

def validate_confidence() -> float:
    default_conf = 0.95
    confidence_input_element = document.querySelector("#confidence_input")
    if confidence_input_element.value in [None, ""]:
        return default_conf
    try:
        confidence = float(confidence_input_element.value) / 100
        if confidence <= 0.001 or confidence > 1:
            raise ValueError
        return confidence
    except ValueError:
        raise ValueError("Confidence level must be a fractional number from 0.1 to 100")

def validate_num_of_experiments() -> int:
    default_num = 5000
    num_of_experiments_element = document.querySelector("#num_of_experiments_input")
    if num_of_experiments_element.value in [None, ""]:
        return default_num
    try:
        num_of_experiments = int(num_of_experiments_element.value)
        if num_of_experiments <= 0:
            raise ValueError
        return num_of_experiments
    except ValueError:
        raise ValueError("Number of experiments must be a positive integer")