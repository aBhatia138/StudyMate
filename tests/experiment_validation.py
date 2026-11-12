from jsonschema import Draft202012Validator

from src.tool_definitions import PERCENTAGE_TOOL

schema = PERCENTAGE_TOOL["function"]["parameters"]

validator = Draft202012Validator(schema)

arguments = {
    "value": 250,
    # "percentage": 15
}

errors = list(validator.iter_errors(arguments))

if not errors:
    print("Arguments are valid. ")

else:
    for error in errors:
        print(error.message)
