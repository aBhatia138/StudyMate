from src.study_functions import (
    percentage_calculator,
    days_until_exam,
    compound_interest_calculator,
    generate_study_plan
)

from src.tool_definitions import (
    PERCENTAGE_TOOL,
    DAYS_UNTIL_EXAM_TOOL,
    COMPOUND_INTEREST_TOOL,
    GENERATE_STUDY_PLAN_TOOL
)

from jsonschema import Draft202012Validator, ValidationError


TOOL_REGISTRY = {
    "percentage_calculator": percentage_calculator,
    "days_until_exam": days_until_exam,
    "compound_interest_calculator": compound_interest_calculator,
    "generate_study_plan": generate_study_plan
}

TOOL_SCHEMAS = {
    "percentage_calculator": PERCENTAGE_TOOL["function"]["parameters"],
    "compound_interest_calculator": COMPOUND_INTEREST_TOOL["function"]["parameters"],
    "days_until_exam": DAYS_UNTIL_EXAM_TOOL["function"]["parameters"],
    "generate_study_plan": GENERATE_STUDY_PLAN_TOOL["function"]["parameters"]
}

def execute_tool(tool_name: str, arguments: dict) -> dict:

    if tool_name not in TOOL_REGISTRY:
        raise ValueError(
            f"Unknown tool: {tool_name}"
        )

    #Check whether arguments are supplied as a dictionary
    if not isinstance(arguments, dict):
        raise TypeError(
            "Tool arguments must be a dictionary. "
        )

    #Retrieve the corresponding JSON schema
    schema = TOOL_SCHEMAS[tool_name]

    #Validate arguments against the schema
    validator = Draft202012Validator(schema)

    try:
        validator.validate(arguments)

    except ValidationError as e:
        raise ValueError(
            f"Invalid arguments for {tool_name}: {e.message}"
        ) from e

    function = TOOL_REGISTRY[tool_name]

    result = function(**arguments)

    return result

