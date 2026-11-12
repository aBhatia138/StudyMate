from jsonschema import Draft202012Validator

PERCENTAGE_TOOL = {
    "type": "function",
    "function": {
        "name": "percentage_calculator",
        "description": (
            "Calculate a specified percetage of a given value. "
        ),
        "parameters": {
            "type": "object",
            "properties": {

                "value": {
                    "type": "number",
                    "description": "The origina; numerical value. "
                },

                "percentage": {
                    "type": "number",
                    "description": "The percentage to calculate. "
                }
            },
            "required": ["value","percentage"]
        }
    }
}

COMPOUND_INTEREST_TOOL = {
    "type": "function",
    "function": {
        "name": "compound_interest_calculator",
        "description": (
            "Calculate the interest gained on investment of "
            "a given principal at a given annual rate over "
            "a given time period in years. "
        ),
        "parameters": {
            "type": "object",
            "properties": {

                "principal": {
                    "type": "number",
                    "description": "The initial principal invested. "
                },

                "annual_rate": {
                    "type": "number",
                    "description": "The annual rate of compounding. "
                },

                "years": {
                    "type": "number",
                    "description": "The duration of compounding in years. "
                }
            },
            "required": ["principal","annual_rate","years"]
        }
    }
}

DAYS_UNTIL_EXAM_TOOL = {
    "type": "function",
    "function": {
        "name": "days_until_exam",
        "description": (
            "Calculate days remaining until exam date. "
        ),
        "parameters": {
            "type": "object",
            "properties": {

                "exam_date": {
                    "type": "string",
                    "description": (
                        "The date of exam expressed in YYYY-MM-DD format. "
                    )

                }
            },
            "required": ["exam_date"]
        }
    }
}

GENERATE_STUDY_PLAN_TOOL = {
    "type": "function",
    "function": {
        "name": "generate_study_plan",
        "description": (
            "Generate a study plan given a list of subjects, "
            "number of available days and the number of hours "
            "to be spent studying per day. "
        ),
        "parameters": {
            "type": "object",
            "properties": {

                "subjects": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": (
                        "A list of subjects to be studied. "
                    )
                },

                "available_days": {
                    "type": "integer",
                    "description": "Number of days before the exam. "
                },

                "hours_per_day": {
                    "type": "number",
                    "description": "Number of hours spent studying per day. "
                }
            },
            "required": ["subjects","available_days","hours_per_day"]
        }
    }
}

TOOLS = [
    PERCENTAGE_TOOL,
    DAYS_UNTIL_EXAM_TOOL,
    GENERATE_STUDY_PLAN_TOOL,
    COMPOUND_INTEREST_TOOL
]

#validating the parametrs schema of tool definitions
for tool in TOOLS:

    parameters_schema = tool["function"]["parameters"]

    try:
        Draft202012Validator.check_schema(parameters_schema)

        print(
            f"{tool['function']['name']}: "
            "Schema is valid. "
        )

    except Exception as e:
        print(
            f"{tool['function']['name']}: "
            f"Invalid schema: {e}"
        )

