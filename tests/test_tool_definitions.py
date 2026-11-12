import unittest
from jsonschema import Draft202012Validator

from src.tool_definitions import (
    PERCENTAGE_TOOL,
    DAYS_UNTIL_EXAM_TOOL,
    COMPOUND_INTEREST_TOOL,
    GENERATE_STUDY_PLAN_TOOL
)

tools = [
    PERCENTAGE_TOOL,
    DAYS_UNTIL_EXAM_TOOL,
    COMPOUND_INTEREST_TOOL,
    GENERATE_STUDY_PLAN_TOOL
]

class TestDefinitions(unittest.TestCase):

    def validate_arguments(self, tool, arguments):

        #validate an argument dictionary against a tool's JSON schema 

        schema = tool["function"]["parameters"]
        validator = Draft202012Validator(schema)
        return list(validator.iter_errors(arguments))

    def test_all_schemas_are_valid(self):

        for tool in tools:
            with self.subTest(tool=tool["function"]["name"]):
                schema = tool["function"]["parameters"]
                Draft202012Validator.check_schema(schema)

    def test_percentage_valid_arguments(self):

        arguments = {
            "value": 850,
            "percentage": 15
        }

        errors = self.validate_arguments(PERCENTAGE_TOOL, arguments)

        self.assertEqual(errors, [])

    def test_percentage_missing_required_argument(self):

        arguments = {
            "value": 100
        }

        errors = self.validate_arguments(PERCENTAGE_TOOL, arguments)

        self.assertNotEqual(errors, [])

    def test_percentage_rejects_string_value(self):

        arguments = {
            "value": "150",
            "percentage": 15
        }

        errors = self.validate_arguments(PERCENTAGE_TOOL, arguments)

        self.assertNotEqual(errors, [])

    def test_compound_interest_valid_arguments(self):

        arguments = {
            "principal": 5000,
            "annual_rate": 6,
            "years": 3
        }

        errors = self.validate_arguments(
            COMPOUND_INTEREST_TOOL,
            arguments
        )

        self.assertEqual(errors, [])

    def test_compound_interest_rejects_string_principal(self):

        arguments = {
            "principal": "5000",
            "annual_rate": 6,
            "years": 3
        }

        errors = self.validate_arguments(COMPOUND_INTEREST_TOOL, arguments)

        self.assertNotEqual(errors, [])

    def test_exam_date_valid_arguments(self):
        arguments = {
            "exam_date": "2026-12-15"
        }

        errors = self.validate_arguments(
            DAYS_UNTIL_EXAM_TOOL,
            arguments
        )

        self.assertEqual(errors, [])

    def test_exam_date_rejects_integer(self):
        arguments = {
            "exam_date": 20261215
        }

        errors = self.validate_arguments(
            DAYS_UNTIL_EXAM_TOOL,
            arguments
        )

        self.assertNotEqual(errors, [])

    def test_exam_date_missing_required_argument(self):
        arguments = {}

        errors = self.validate_arguments(
            DAYS_UNTIL_EXAM_TOOL,
            arguments
        )

        self.assertNotEqual(errors, [])

    # --------------------------------------------------
    # 5. Study plan generator tests
    # --------------------------------------------------

    def test_study_plan_valid_arguments(self):
        arguments = {
            "subjects": ["Mathematics", "Statistics", "Finance"],
            "available_days": 10,
            "hours_per_day": 4
        }

        errors = self.validate_arguments(
            GENERATE_STUDY_PLAN_TOOL,
            arguments
        )

        self.assertEqual(errors, [])

    def test_study_plan_rejects_numeric_subjects(self):
        arguments = {
            "subjects": ["Mathematics", 123, "Finance"],
            "available_days": 10,
            "hours_per_day": 4
        }

        errors = self.validate_arguments(
            GENERATE_STUDY_PLAN_TOOL,
            arguments
        )

        self.assertNotEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
